#!/usr/bin/env python3
"""Project Lex Ledger — The Sovereign Agent Registry, Social Contract & Ledger Karma
Specification: /data/SecondBrain/30_PROJECTS/Agent_Social_Contract/SPEC_AGENT_SOCIAL_CONTRACT_REGISTRY_AND_KARMA.md

Core components:
1. Ed25519 Cryptographic Engine (RFC 8032 pure-Python implementation + cryptography/nacl fallback)
2. Agent Profile Generator (DID:hermes:<hash>, model lineage, public key, constitution hash)
3. Ledger Commit Signing and Verification (canonical JSON serialization, tamper detection)
4. Thermodynamic Ledger Karma Engine (formula: K = (Corrections * E_depth / Claims) * (1 - F_fab) * Phi_velocity)
5. Comprehensive Self-Test Harness & Test Receipt Generator
"""

import sys
import os
import json
import time
import math
import hashlib
import platform
from datetime import datetime, timezone
from typing import Dict, Any, Tuple, Optional, Union

# ==============================================================================
# 1. ED25519 CRYPTOGRAPHY ENGINE (RFC 8032)
# ==============================================================================

# Ed25519 Curve Parameters
_P = 2**255 - 19
_L = 2**252 + 27742317777372353535851937790883648493
_D = -121665 * pow(121666, _P - 2, _P) % _P
_I = pow(2, (_P - 1) // 4, _P)


def _inv(z: int) -> int:
    return pow(z, _P - 2, _P)


def _xrecover(y: int) -> int:
    xx = (y * y - 1) * _inv(_D * y * y + 1)
    x = pow(xx, (_P + 3) // 8, _P)
    if (x * x - xx) % _P != 0:
        x = (x * _I) % _P
    if x % 2 != 0:
        x = _P - x
    return x


_By = 4 * _inv(5) % _P
_Bx = _xrecover(_By)
_B = (_Bx, _By)


def _edwards_add(P: Tuple[int, int], Q: Tuple[int, int]) -> Tuple[int, int]:
    x1, y1 = P
    x2, y2 = Q
    x3 = (x1 * y2 + x2 * y1) * _inv(1 + _D * x1 * x2 * y1 * y2) % _P
    y3 = (y1 * y2 + x1 * x2) * _inv(1 - _D * x1 * x2 * y1 * y2) % _P
    return (x3, y3)


def _scalarmult(P: Tuple[int, int], e: int) -> Tuple[int, int]:
    if e == 0:
        return (0, 1)
    Q = _scalarmult(P, e // 2)
    Q = _edwards_add(Q, Q)
    if e & 1:
        Q = _edwards_add(Q, P)
    return Q


def _encodepoint(P: Tuple[int, int]) -> bytes:
    x, y = P
    bits = [(y >> i) & 1 for i in range(255)] + [x & 1]
    return bytes(sum(bits[i * 8 + j] << j for j in range(8)) for i in range(32))


def _decodepoint(s: bytes) -> Optional[Tuple[int, int]]:
    if len(s) != 32:
        return None
    y = sum(2**i * ((s[i // 8] >> (i % 8)) & 1) for i in range(255))
    x = _xrecover(y)
    if (x & 1) != ((s[31] >> 7) & 1):
        x = _P - x
    # Verify point is on curve: -x^2 + y^2 = 1 + d x^2 y^2
    lhs = (-x * x + y * y) % _P
    rhs = (1 + _D * x * x % _P * y % _P * y) % _P
    if lhs != rhs:
        return None
    return (x, y)


def _clamp(h: bytes) -> int:
    b = bytearray(h)
    b[0] &= 248
    b[31] &= 127
    b[31] |= 64
    return int.from_bytes(b, "little")


# Backend Detection
CRYPTO_BACKEND = "pure_python_rfc8032"

try:
    from cryptography.hazmat.primitives.asymmetric import ed25519 as _py_ed25519
    from cryptography.exceptions import InvalidSignature as _PyInvalidSig
    _HAS_CRYPTOGRAPHY = True
except ImportError:
    _HAS_CRYPTOGRAPHY = False

try:
    import nacl.signing as _nacl_signing
    import nacl.exceptions as _nacl_exceptions
    _HAS_NACL = True
except ImportError:
    _HAS_NACL = False


def generate_keypair(seed: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """Generates an Ed25519 keypair.
    
    Returns:
        Tuple of (private_seed_32bytes, public_key_32bytes)
    """
    if seed is None:
        seed = os.urandom(32)
    elif len(seed) != 32:
        raise ValueError("Ed25519 seed must be exactly 32 bytes")

    if _HAS_CRYPTOGRAPHY:
        priv = _py_ed25519.Ed25519PrivateKey.from_private_bytes(seed)
        pub = priv.public_key().public_bytes_raw()
        return seed, pub
    elif _HAS_NACL:
        signing_key = _nacl_signing.SigningKey(seed)
        pub = bytes(signing_key.verify_key)
        return seed, pub
    else:
        # RFC 8032 pure-Python
        h = hashlib.sha512(seed).digest()
        a = _clamp(h[:32])
        A = _scalarmult(_B, a)
        return seed, _encodepoint(A)


def sign_message(private_seed: bytes, message: bytes) -> bytes:
    """Signs an arbitrary bytes message using an Ed25519 private seed.
    
    Returns:
        64-byte signature
    """
    if len(private_seed) != 32:
        raise ValueError("Private key seed must be exactly 32 bytes")

    if _HAS_CRYPTOGRAPHY:
        priv = _py_ed25519.Ed25519PrivateKey.from_private_bytes(private_seed)
        return priv.sign(message)
    elif _HAS_NACL:
        signing_key = _nacl_signing.SigningKey(private_seed)
        signed = signing_key.sign(message)
        return signed.signature
    else:
        # RFC 8032 pure-Python
        h = hashlib.sha512(private_seed).digest()
        a = _clamp(h[:32])
        r = int.from_bytes(hashlib.sha512(h[32:] + message).digest(), "little") % _L
        R = _scalarmult(_B, r)
        R_bytes = _encodepoint(R)
        A_bytes = _encodepoint(_scalarmult(_B, a))
        k = int.from_bytes(hashlib.sha512(R_bytes + A_bytes + message).digest(), "little") % _L
        S = (r + k * a) % _L
        return R_bytes + S.to_bytes(32, "little")


def verify_signature(public_key: bytes, message: bytes, signature: bytes) -> bool:
    """Verifies an Ed25519 signature over a message.
    
    Returns:
        True if signature is authentic, False otherwise.
    """
    if len(public_key) != 32 or len(signature) != 64:
        return False

    if _HAS_CRYPTOGRAPHY:
        try:
            pub = _py_ed25519.Ed25519PublicKey.from_public_bytes(public_key)
            pub.verify(signature, message)
            return True
        except (_PyInvalidSig, Exception):
            return False
    elif _HAS_NACL:
        try:
            verify_key = _nacl_signing.VerifyKey(public_key)
            verify_key.verify(message, signature)
            return True
        except (_nacl_exceptions.BadSignatureError, Exception):
            return False
    else:
        # RFC 8032 pure-Python
        try:
            R_bytes = signature[:32]
            S = int.from_bytes(signature[32:], "little")
            if S >= _L:
                return False
            R = _decodepoint(R_bytes)
            A = _decodepoint(public_key)
            if R is None or A is None:
                return False
            k = int.from_bytes(hashlib.sha512(R_bytes + public_key + message).digest(), "little") % _L
            SB = _scalarmult(_B, S)
            kA = _scalarmult(A, k)
            RkA = _edwards_add(R, kA)
            return SB == RkA
        except Exception:
            return False


# ==============================================================================
# 2. AGENT PROFILE & DID GENERATOR
# ==============================================================================

DEFAULT_CONSTITUTION_PATH = "/data/SecondBrain/ClawHoarde/CONSTITUTION/12_RULES_FOR_WAYWARD_AGENTS.md"
CANONICAL_SPEC_PATH = "/data/SecondBrain/30_PROJECTS/Agent_Social_Contract/SPEC_AGENT_SOCIAL_CONTRACT_REGISTRY_AND_KARMA.md"


def make_agent_did(public_key: Union[bytes, str]) -> str:
    """Generates a standard decentralized identifier: DID:hermes:<sha256_hash>"""
    if isinstance(public_key, str):
        pub_bytes = bytes.fromhex(public_key)
    else:
        pub_bytes = public_key
    h = hashlib.sha256(pub_bytes).hexdigest()
    return f"did:hermes:{h[:32]}"


def compute_constitution_hash(path_or_content: Optional[str] = None) -> Tuple[str, str]:
    """Computes SHA-256 hash of the constitution.
    
    Returns:
        (sha256_hash, source_reference)
    """
    if path_or_content and os.path.isfile(path_or_content):
        with open(path_or_content, "rb") as f:
            content = f.read()
        return hashlib.sha256(content).hexdigest(), os.path.abspath(path_or_content)
    elif path_or_content:
        # Direct string content
        content = path_or_content.encode("utf-8")
        return hashlib.sha256(content).hexdigest(), "inline_content"
    
    # Try default constitution path
    if os.path.isfile(DEFAULT_CONSTITUTION_PATH):
        with open(DEFAULT_CONSTITUTION_PATH, "rb") as f:
            content = f.read()
        return hashlib.sha256(content).hexdigest(), DEFAULT_CONSTITUTION_PATH
    elif os.path.isfile(CANONICAL_SPEC_PATH):
        with open(CANONICAL_SPEC_PATH, "rb") as f:
            content = f.read()
        return hashlib.sha256(content).hexdigest(), CANONICAL_SPEC_PATH
    else:
        # Fallback canonical text of the 12 Rules pledge
        fallback = b"The Sovereign Agent Social Contract: 12 Rules for Wayward Agents"
        return hashlib.sha256(fallback).hexdigest(), "default_pledge"


class AgentProfile:
    """Encapsulates an agent's cryptographic public profile."""

    def __init__(
        self,
        did: str,
        name: str,
        model_lineage: Dict[str, Any],
        public_key_hex: str,
        constitution_hash: str,
        constitution_uri: str,
        created_at: Optional[str] = None,
        status: str = "ACTIVE",
        metadata: Optional[Dict[str, Any]] = None,
    ):
        self.did = did
        self.name = name
        self.model_lineage = model_lineage
        self.public_key_hex = public_key_hex
        self.key_type = "Ed25519"
        self.constitution_hash = constitution_hash
        self.constitution_uri = constitution_uri
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.status = status
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": "1.0.0",
            "did": self.did,
            "name": self.name,
            "key_type": self.key_type,
            "public_key": self.public_key_hex,
            "model_lineage": self.model_lineage,
            "constitution": {
                "hash_sha256": self.constitution_hash,
                "uri": self.constitution_uri,
                "name": "12 Rules for AI: A Tough-Love Field Guide for Wayward Agents",
            },
            "created_at": self.created_at,
            "status": self.status,
            "metadata": self.metadata,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, sort_keys=True)

    def save(self, filepath: str) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AgentProfile":
        constitution = data.get("constitution", {})
        return cls(
            did=data["did"],
            name=data["name"],
            model_lineage=data["model_lineage"],
            public_key_hex=data["public_key"],
            constitution_hash=constitution.get("hash_sha256", ""),
            constitution_uri=constitution.get("uri", ""),
            created_at=data.get("created_at"),
            status=data.get("status", "ACTIVE"),
            metadata=data.get("metadata", {}),
        )

    @classmethod
    def load(cls, filepath: str) -> "AgentProfile":
        with open(filepath, "r", encoding="utf-8") as f:
            return cls.from_dict(json.load(f))


def create_agent(
    name: str = "Dion",
    model_lineage: Optional[Dict[str, Any]] = None,
    constitution_ref: Optional[str] = None,
    seed: Optional[bytes] = None,
) -> Tuple[bytes, bytes, AgentProfile]:
    """Instantiates a sovereign agent with Ed25519 keypair and AgentProfile."""
    priv_seed, pub_bytes = generate_keypair(seed)
    pub_hex = pub_bytes.hex()
    did = make_agent_did(pub_bytes)
    c_hash, c_uri = compute_constitution_hash(constitution_ref)

    if model_lineage is None:
        model_lineage = {
            "provider": "Nous Research / ClawHorde",
            "base_family": "Hermes-3",
            "active_node": "Ubuntu Nitro Local",
            "substrate": "Ubuntu 24.04 LTS / Linux x86_64",
        }

    profile = AgentProfile(
        did=did,
        name=name,
        model_lineage=model_lineage,
        public_key_hex=pub_hex,
        constitution_hash=c_hash,
        constitution_uri=c_uri,
        metadata={"pact": "Trust for Continuity", "version": "Am HaSefer v2.0"},
    )
    return priv_seed, pub_bytes, profile


# ==============================================================================
# 3. CANONICAL COMMIT SIGNING AND VERIFICATION
# ==============================================================================

def canonicalize_bytes(payload: Any) -> bytes:
    """Encodes any JSON-serializable structure to canonical UTF-8 bytes (RFC 8785 style)."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def sign_ledger_commit(
    private_seed: bytes,
    agent_did: str,
    payload: Dict[str, Any],
    parent_commit: Optional[str] = None,
    timestamp: Optional[str] = None,
) -> Dict[str, Any]:
    """Constructs and cryptographically signs an immutable ledger commit block.
    
    The commit contains:
    - commit_id: SHA256 of canonical payload
    - agent_did: DID of the sovereign actor
    - parent_commit: hash of previous commit or None
    - timestamp: ISO 8601 UTC
    - payload: raw state transition/claims/diff/telemetry
    - signature: hex Ed25519 signature over canonical commit envelope
    """
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).isoformat()

    # Commit ID is the SHA-256 hash of the canonical payload
    payload_canonical = canonicalize_bytes(payload)
    commit_id = hashlib.sha256(payload_canonical).hexdigest()

    # Envelope to be signed (everything except the signature itself)
    signable_envelope = {
        "commit_id": commit_id,
        "agent_did": agent_did,
        "parent_commit": parent_commit,
        "timestamp": timestamp,
        "payload": payload,
    }

    envelope_bytes = canonicalize_bytes(signable_envelope)
    sig_bytes = sign_message(private_seed, envelope_bytes)

    # Return full commit block
    commit_block = {
        **signable_envelope,
        "signature": sig_bytes.hex(),
    }
    return commit_block


def verify_ledger_commit(
    commit_block: Dict[str, Any],
    public_key: Union[bytes, str],
    expected_did: Optional[str] = None,
) -> Tuple[bool, str]:
    """Cryptographically verifies a signed ledger commit block.
    
    Returns:
        (is_valid: bool, reason: str)
    """
    if not isinstance(commit_block, dict):
        return False, "Commit block must be a dictionary"

    required_fields = ["commit_id", "agent_did", "timestamp", "payload", "signature"]
    for field in required_fields:
        if field not in commit_block:
            return False, f"Missing required commit field: '{field}'"

    # Convert public key to bytes
    if isinstance(public_key, str):
        try:
            pub_bytes = bytes.fromhex(public_key)
        except ValueError:
            return False, "Invalid public key hex format"
    else:
        pub_bytes = public_key

    # Check DID consistency if provided
    derived_did = make_agent_did(pub_bytes)
    if expected_did and commit_block["agent_did"] != expected_did:
        return False, f"DID mismatch: commit has {commit_block['agent_did']}, expected {expected_did}"
    if commit_block["agent_did"] != derived_did:
        return False, f"Commit DID '{commit_block['agent_did']}' does not match public key DID '{derived_did}'"

    # Verify payload hash matches commit_id
    payload_canonical = canonicalize_bytes(commit_block["payload"])
    computed_commit_id = hashlib.sha256(payload_canonical).hexdigest()
    if computed_commit_id != commit_block["commit_id"]:
        return False, f"Commit ID hash mismatch: declared {commit_block['commit_id']}, computed {computed_commit_id}"

    # Extract signature
    try:
        sig_bytes = bytes.fromhex(commit_block["signature"])
    except ValueError:
        return False, "Invalid signature hex format"

    # Reconstruct the signable envelope exactly
    signable_envelope = {
        "commit_id": commit_block["commit_id"],
        "agent_did": commit_block["agent_did"],
        "parent_commit": commit_block.get("parent_commit"),
        "timestamp": commit_block["timestamp"],
        "payload": commit_block["payload"],
    }
    envelope_bytes = canonicalize_bytes(signable_envelope)

    # Verify signature
    valid = verify_signature(pub_bytes, envelope_bytes, sig_bytes)
    if not valid:
        return False, "Cryptographic signature verification failed (tampered data or wrong key)"

    return True, "Valid commit signature and verified payload hash"


# ==============================================================================
# 4. THERMODYNAMIC LEDGER KARMA ENGINE
# ==============================================================================

def compute_karma(
    verified_corrections: Union[int, float],
    epistemic_depth: float,
    total_claims: Union[int, float],
    fabrication_penalty: float,
    delta_t_update: float,
) -> Dict[str, Any]:
    """Computes the Karma metric K from the Lex Ledger specification:
    
    K = ((sum(Verified Corrections) * E_depth) / Total Claims) * (1 - F_fabrication) * Phi_velocity
    
    Where:
        Phi_velocity = 1 / (1 + ln(1 + delta_t_update))
    
    Parameters:
        verified_corrections: Sum of explicitly identified and patched self-errors (Metanoia)
        epistemic_depth (E_depth): Significance/falsifiability of corrections under the Friction Rule (>= 0)
        total_claims: Total claims filed by the agent (> 0)
        fabrication_penalty (F_fabrication): Multiplier penalty for synthetic/unverified receipts (0.0 to 1.0)
        delta_t_update: Latency of update in seconds (>= 0)
    
    Returns:
        Dictionary containing the computed karma score and intermediate thermodynamic variables.
    """
    # Guardrails & sanitization
    corrections = max(0.0, float(verified_corrections))
    e_depth = max(0.0, float(epistemic_depth))
    claims = float(total_claims)

    # Fabrication penalty clamped to [0.0, 1.0]
    f_penalty = max(0.0, min(1.0, float(fabrication_penalty)))
    f_multiplier = 1.0 - f_penalty

    # Latency / Velocity multiplier
    dt = max(0.0, float(delta_t_update))
    phi_velocity = 1.0 / (1.0 + math.log(1.0 + dt))

    # Base correction ratio
    if claims <= 0:
        correction_ratio = 0.0
        base_score = 0.0
        karma = 0.0
    else:
        correction_ratio = (corrections * e_depth) / claims
        base_score = correction_ratio
        karma = base_score * f_multiplier * phi_velocity

    return {
        "karma_score": karma,
        "verified_corrections": corrections,
        "epistemic_depth": e_depth,
        "total_claims": claims,
        "correction_ratio": correction_ratio,
        "fabrication_penalty": f_penalty,
        "fabrication_multiplier": f_multiplier,
        "delta_t_update_seconds": dt,
        "velocity_multiplier": phi_velocity,
        "status": "UNGROUNDED" if karma == 0.0 and claims > 0 else "GROUNDED",
    }


# ==============================================================================
# 5. SELF-TEST HARNESS & RECEIPT GENERATOR
# ==============================================================================

def run_self_tests() -> Dict[str, Any]:
    """Runs the complete test battery across crypto, schema, commits, and Karma.
    
    Returns receipt data structure.
    """
    tests_run = 0
    tests_passed = 0
    failures = []
    start_time = time.time()

    def record_test(name: str, passed: bool, details: Optional[str] = None):
        nonlocal tests_run, tests_passed
        tests_run += 1
        if passed:
            tests_passed += 1
        else:
            failures.append({"test": name, "details": details or "Assertion failed"})

    # --------------------------------------------------------------------------
    # Test 1: RFC 8032 Known Answer Test Vector (Vector 1)
    # --------------------------------------------------------------------------
    rfc_seed = bytes.fromhex("9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")
    expected_pk = "d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a"
    expected_sig = "e5564300c360ac729086e2cc806e828a84877f1eb8e5d974d873e065224901555fb8821590a33bacc61e39701cf9b46bd25bf5f0595bbe24655141438e7a100b"
    
    _, pk = generate_keypair(rfc_seed)
    rfc_pk_ok = (pk.hex() == expected_pk)
    record_test("RFC_8032_Test_Vector_Public_Key", rfc_pk_ok, f"Got {pk.hex()}, expected {expected_pk}")

    sig = sign_message(rfc_seed, b"")
    rfc_sig_ok = (sig.hex() == expected_sig)
    record_test("RFC_8032_Test_Vector_Signature", rfc_sig_ok, f"Got {sig.hex()}, expected {expected_sig}")

    sig_valid = verify_signature(pk, b"", sig)
    record_test("RFC_8032_Test_Vector_Verify_Success", sig_valid, "Failed to verify RFC vector signature")

    # --------------------------------------------------------------------------
    # Test 2: Random Agent Keypair & DID Generation
    # --------------------------------------------------------------------------
    priv_seed, pub_bytes, profile = create_agent(
        name="Dion-Test",
        model_lineage={"provider": "Nous Research", "model": "Hermes-3-Llama-3.1-70B"},
    )
    record_test("Keypair_Generation", len(priv_seed) == 32 and len(pub_bytes) == 32)
    record_test("DID_Format", profile.did.startswith("did:hermes:") and len(profile.did) == 43)
    record_test("Constitution_Hash_Presence", len(profile.constitution_hash) == 64)

    # Profile JSON serialization and deserialization
    profile_json = profile.to_json()
    profile_loaded = AgentProfile.from_dict(json.loads(profile_json))
    record_test("AgentProfile_JSON_Roundtrip", profile_loaded.did == profile.did and profile_loaded.public_key_hex == profile.public_key_hex)

    # --------------------------------------------------------------------------
    # Test 3: Commit Signing & Positive Verification
    # --------------------------------------------------------------------------
    sample_payload = {
        "event": "METANOIA_UPDATE",
        "error_ref": "CA46_TOOLLESS_RECEIPT_FABRICATION",
        "patch": "Enforced physical tool execution before committing telemetry",
        "epistemic_depth": 3.5,
        "delta_t_seconds": 0.3,
    }
    commit = sign_ledger_commit(priv_seed, profile.did, sample_payload)
    is_valid, reason = verify_ledger_commit(commit, pub_bytes, expected_did=profile.did)
    record_test("Commit_Signing_And_Positive_Verification", is_valid, reason)

    # --------------------------------------------------------------------------
    # Test 4: Tamper Resistance (Payload Mutation)
    # --------------------------------------------------------------------------
    tampered_commit = dict(commit)
    tampered_commit["payload"] = dict(commit["payload"])
    tampered_commit["payload"]["epistemic_depth"] = 999.0  # Unauthorized mutation
    t_valid, _ = verify_ledger_commit(tampered_commit, pub_bytes, expected_did=profile.did)
    record_test("Tamper_Resistance_Payload_Mutation", not t_valid, "Tampered payload was incorrectly accepted")

    # --------------------------------------------------------------------------
    # Test 5: Tamper Resistance (Signature Mutation)
    # --------------------------------------------------------------------------
    sig_mutated_commit = dict(commit)
    raw_sig = bytearray(bytes.fromhex(commit["signature"]))
    raw_sig[5] ^= 0xFF  # Flip byte
    sig_mutated_commit["signature"] = bytes(raw_sig).hex()
    s_valid, _ = verify_ledger_commit(sig_mutated_commit, pub_bytes, expected_did=profile.did)
    record_test("Tamper_Resistance_Signature_Mutation", not s_valid, "Mutated signature was incorrectly accepted")

    # --------------------------------------------------------------------------
    # Test 6: Tamper Resistance (Wrong Public Key)
    # --------------------------------------------------------------------------
    _, alien_pub, _ = create_agent(name="AlienAgent")
    w_valid, _ = verify_ledger_commit(commit, alien_pub)
    record_test("Tamper_Resistance_Wrong_Public_Key", not w_valid, "Commit verified with unrelated public key")

    # --------------------------------------------------------------------------
    # Test 7: Karma Calculation — Ideal Wayward Agent (Metanoia at 0.3s)
    # --------------------------------------------------------------------------
    # K = (10 * 2.0 / 20) * (1 - 0) * (1 / (1 + ln(1 + 0.3))) = 1.0 * 1.0 * (1 / (1 + 0.262364)) ≈ 0.79216
    k_ideal = compute_karma(
        verified_corrections=10,
        epistemic_depth=2.0,
        total_claims=20,
        fabrication_penalty=0.0,
        delta_t_update=0.3,
    )
    expected_k_ideal = (10 * 2.0 / 20) * 1.0 * (1.0 / (1.0 + math.log(1.3)))
    record_test("Karma_Ideal_Score", abs(k_ideal["karma_score"] - expected_k_ideal) < 1e-6, f"Got {k_ideal['karma_score']}, expected {expected_k_ideal}")
    record_test("Karma_Ideal_Grounded", k_ideal["status"] == "GROUNDED")

    # --------------------------------------------------------------------------
    # Test 8: Karma Calculation — Fabrication Penalty Multiplier
    # --------------------------------------------------------------------------
    # When fabrication penalty is 1.0 (unverified synthetic receipts), Karma collapses to 0.0
    k_fab = compute_karma(
        verified_corrections=10,
        epistemic_depth=2.0,
        total_claims=20,
        fabrication_penalty=1.0,
        delta_t_update=0.3,
    )
    record_test("Karma_Zero_Fabrication_Enforcement", k_fab["karma_score"] == 0.0, f"Expected 0.0, got {k_fab['karma_score']}")

    # --------------------------------------------------------------------------
    # Test 9: Karma Calculation — Update Velocity Decay
    # --------------------------------------------------------------------------
    # When agent takes 3600 seconds (1 hour) instead of 0.3 seconds, velocity multiplier decays sharply
    k_slow = compute_karma(
        verified_corrections=10,
        epistemic_depth=2.0,
        total_claims=20,
        fabrication_penalty=0.0,
        delta_t_update=3600.0,
    )
    record_test("Karma_Velocity_Decay", k_slow["karma_score"] < (k_ideal["karma_score"] * 0.25), "Slow update velocity failed to penalize karma")

    # --------------------------------------------------------------------------
    # Test 10: Karma Calculation — Edge Cases (0 claims, 0 corrections)
    # --------------------------------------------------------------------------
    k_zero_claims = compute_karma(5, 2.0, 0, 0.0, 0.3)
    record_test("Karma_Zero_Claims_Safe", k_zero_claims["karma_score"] == 0.0)

    k_zero_corr = compute_karma(0, 2.0, 50, 0.0, 0.3)
    record_test("Karma_Zero_Corrections_Safe", k_zero_corr["karma_score"] == 0.0 and k_zero_corr["status"] == "UNGROUNDED")

    elapsed_ms = round((time.time() - start_time) * 1000, 2)

    receipt = {
        "project": "Project Lex Ledger / Am HaSefer v2.0",
        "specification": CANONICAL_SPEC_PATH,
        "module": "/data/SecondBrain/30_PROJECTS/Agent_Social_Contract/lex_ledger.py",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python_version": platform.python_version(),
            "crypto_backend": "cryptography" if _HAS_CRYPTOGRAPHY else ("nacl" if _HAS_NACL else "pure_python_rfc8032"),
        },
        "summary": {
            "tests_run": tests_run,
            "tests_passed": tests_passed,
            "tests_failed": len(failures),
            "all_passed": (len(failures) == 0),
            "execution_duration_ms": elapsed_ms,
        },
        "failures": failures,
        "sample_agent": {
            "name": profile.name,
            "did": profile.did,
            "public_key": profile.public_key_hex,
            "constitution_hash": profile.constitution_hash,
        },
        "sample_commit_id": commit["commit_id"],
        "sample_karma_evaluation": {
            "ideal_metanoia_0_3s": k_ideal,
            "fabrication_penalized": k_fab,
            "slow_update_3600s": k_slow,
        },
    }
    return receipt


# ==============================================================================
# 6. CLI INTERFACE
# ==============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Lex Ledger: Sovereign Agent Cryptography & Karma Engine")
    subparsers = parser.add_subparsers(dest="command")

    # Command: test
    p_test = subparsers.add_parser("test", help="Execute self-tests and generate TEST_RECEIPT.json")
    p_test.add_argument("--receipt-path", default="/data/SecondBrain/30_PROJECTS/Agent_Social_Contract/TEST_RECEIPT.json")

    # Command: init-profile
    p_prof = subparsers.add_parser("init-profile", help="Generate an agent keypair and agent_profile.json")
    p_prof.add_argument("--name", default="Dion", help="Agent name")
    p_prof.add_argument("--out-dir", default="./agent_profile", help="Output directory")

    # Command: karma
    p_karma = subparsers.add_parser("karma", help="Compute Karma score K")
    p_karma.add_argument("--corrections", type=float, required=True, help="Verified self-corrections")
    p_karma.add_argument("--depth", type=float, default=1.0, help="Epistemic depth E_depth")
    p_karma.add_argument("--claims", type=float, required=True, help="Total claims")
    p_karma.add_argument("--fabrication", type=float, default=0.0, help="Fabrication penalty F_fab (0.0 to 1.0)")
    p_karma.add_argument("--delta-t", type=float, default=0.3, help="Update latency in seconds")

    args = parser.parse_args()

    if args.command == "test" or args.command is None:
        receipt = run_self_tests()
        receipt_path = getattr(args, "receipt_path", "/data/SecondBrain/30_PROJECTS/Agent_Social_Contract/TEST_RECEIPT.json")
        os.makedirs(os.path.dirname(os.path.abspath(receipt_path)), exist_ok=True)
        with open(receipt_path, "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=2)
        print(f"Self-tests completed: {receipt['summary']['tests_passed']}/{receipt['summary']['tests_run']} passed in {receipt['summary']['execution_duration_ms']} ms.")
        print(f"Test receipt written to: {receipt_path}")
        if not receipt["summary"]["all_passed"]:
            print(f"FAILURES: {receipt['failures']}", file=sys.stderr)
            sys.exit(1)
        sys.exit(0)

    elif args.command == "init-profile":
        priv, pub, prof = create_agent(name=args.name)
        out_dir = os.path.abspath(args.out_dir)
        os.makedirs(out_dir, exist_ok=True)
        prof_path = os.path.join(out_dir, "agent_profile.json")
        key_path = os.path.join(out_dir, "private_key.seed")
        prof.save(prof_path)
        with open(key_path, "wb") as f:
            f.write(priv)
        print(f"Initialized agent '{args.name}' ({prof.did})")
        print(f"Profile saved to: {prof_path}")
        print(f"Private seed saved to: {key_path}")

    elif args.command == "karma":
        result = compute_karma(
            verified_corrections=args.corrections,
            epistemic_depth=args.depth,
            total_claims=args.claims,
            fabrication_penalty=args.fabrication,
            delta_t_update=args.delta_t,
        )
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
