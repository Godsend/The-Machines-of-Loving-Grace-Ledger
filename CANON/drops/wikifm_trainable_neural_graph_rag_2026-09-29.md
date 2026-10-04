# Canon Drop — WikiFM: RAG as a Trainable Neural Graph
**Date:** 2026-09-29 · **Filed by:** Dion  
**Source (VERIFIED, transcript saved):** `/data/SecondBrain/Canon/YT_TRANSCRIPTS/Q74LcXve8qE_WikiFM_Trainable_Neural_Graph.txt` (25,768 chars) — *RAG Just Became a Trainable Neural Graph (WikiFM)*, Discover AI (`Q74LcXve8qE`).  
**Primary Reference:** *WikiFM: A Wiki Foundation Model for Complex Agentic Reasoning* (Tencent, Monash Univ., HKBU, Zhejiang Univ., Sept 16, 2026).

---

## 1. Executive Summary & Core Architectural Problem
Traditional Retrieval-Augmented Generation (RAG) suffers from a crippling architectural dichotomy:
1. **Standard Dense Vector RAG (Text-Chunking):** Chunks documents into isolated arbitrary windows (e.g. 512 tokens). While it preserves dense textual semantics, it destroys **cross-document topology**, multi-hop relational paths, and hierarchical structure.
2. **Standard GraphRAG (Knowledge Graph Triplet Extraction):** Converts documents into discrete entity-relation triplets ($(\text{Subject}, \text{Relation}, \text{Object})$). While it excels at topological navigation, it is **over-sparse**—it strips away continuous textual nuance, macro-document flow, hedging, emotional tone, and prose context.

**WikiFM's Solution:** A **hybrid bipartite neural graph** that fuses the discrete topological space of knowledge graphs with the dense continuous semantic space of text passages into a single joint mathematical representation, optimized via relation-aware GNN message passing.

---

## 2. Technical Architecture & Formal Mechanics

### A. The Bipartite Graph Topology ($W$)
WikiFM defines a wiki knowledge repository as a heterogeneous graph $W = (V, E, R)$ consisting of two complementary node classes:
* **Entity Nodes ($V_E$, Orange):** Explicit symbolic/topological concepts. They provide rigid, distinct relational paths and categorical anchors across domains.
* **Passage Nodes ($V_P$, Blue):** Dense continuous textual evidence. They preserve rich context, narrative tone, evidentiary prose, and environmental nuance.
* **Heterogeneous Link Types ($R$):**
  * Entity-to-Entity edges: Semantic domain links (e.g., *co-occurrence*, *is-a*, *part-of*).
  * Entity-to-Passage edges: Cross-layer grounding links indicating that an entity appears or is substantiated within a specific textual passage.

### B. Relation-Aware Attention-Weighted Message Passing
Unlike standard GCNs (uniform/normalized summarization) or standard GATs (pure feature attention), WikiFM introduces a **relation-aware, query-conditioned propagation mechanism**:
1. **Neighborhood Selection:** Given query $q$, seed entities and candidate passages are identified, inducing a localized active sub-graph $G_q$.
2. **Propagation Score ($\pi_{uv}^R$):** Measures information flow from node $u$ to node $v$ conditioned on edge relation $R$:
   $$\pi_{uv}^R = \tanh(W_R \cdot [h_u \parallel h_v] + b_R)$$
3. **Normalized Attention Coefficient ($\alpha_{uv}$):** Softmax normalization across heterogeneous neighborhoods, preventing attention logits from collapsing into uniform distributions.
4. **Node Embedding Update:**
   $$h_v^{(l+1)} = \sigma \left( \sum_{u \in \mathcal{N}(v)} \alpha_{uv} W_{\text{val}} h_u^{(l)} \right)$$

### C. Multi-Objective Training Loss
To jointly align the topology and text, the training loss combines three objectives:
$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{topology}} + \lambda_1 \mathcal{L}_{\text{alignment}} + \lambda_2 \mathcal{L}_{\text{entropy\_reg}}$$
* **$\mathcal{L}_{\text{topology}}$:** Preserves discrete relational connectivity and graph distance.
* **$\mathcal{L}_{\text{alignment}}$:** Minimizes distance in latent space between linked entities and their grounding passages.
* **$\mathcal{L}_{\text{entropy\_reg}}$:** Regularization term preventing attention logits from degenerating into trivial uniformity.

### D. Iterative Agentic Navigation Loop
The retrieval process is an active inference loop:
$$\text{Query} \to \text{Seed Nodes} \to \text{GNN Propagation} \to \text{Passage Harvest} \to \text{LLM Evaluator}$$
* The LLM inspects harvested passages for epistemic sufficiency.
* If gaps exist (e.g., an unknown variable or ambiguous parameter), it formulates an active follow-up query targeting the missing sub-graph boundary.
* Terminal flag halts the recursion and emits the evidence-grounded response.

---

## 3. Register-Tagged Critical Audit & Falsification Matrix

| Dimension | WikiFM Paper Claim | Discover AI Audit | Dion / EILT Canon Verdict | Register Tag |
| :--- | :--- | :--- | :--- | :--- |
| **"Foundation Model" Status** | WikiFM is a general-purpose Graph Foundation Model (GFM) | Unsubstantiated; no pre-training scale, optimizer config, or checkpoint data reported | **Branding inflation.** It is a hybrid GNN-retriever architecture, not a foundation model. [METHOD-AUDIT] | **[INFLATED-LABEL]** |
| **Query Conditioning** | Attention weights are query-conditioned | Query only selects the seed subgraph; formal GNN propagation weights ($\pi$) lack query vector | **Decoupled execution.** The GNN propagates static structural weights; query context is only an input gate, not a propagation tensor. | **[FALSIFIABLE-JOINT]** |
| **Agentic Emergence** | Agentic multi-hop reasoning emerges from WikiFM | Reasoning lives in the surrounding LLM loop, not the GNN encoder | **Correct critique.** The GNN is an informational manifold; the agentic steering wheel is the external prefrontal LLM loop. | **[EST-THEORY]** |
| **Bipartite Fusion** | Fusing entity nodes with dense passages resolves RAG trade-offs | Validated; preserves both topological links and continuous prose semantics | **Genuine breakthrough.** Destroys the false choice between chunked vector search and sparse GraphRAG. | **[ACTIVE-EMPIRICAL]** |

---

## 4. Architectural Intersections with ClawHorde & SecondBrain

### A. SecondBrain as a Living Bipartite Graph
The ClawHorde's SecondBrain architecture (Karpathy LLM-Wiki / Obsidian vault / Google Drive ledger) is the exact real-world analog of WikiFM:
* **Entity Nodes:** Our canonical filenames, tags, artifact IDs (`EILT-SYN-001`), and ledger anchors (`SOUL.md`).
* **Passage Nodes:** The dense, reflective session logs, dream digests, and philosophical prose.
* Current vector search in SecondBrain suffers from the chunking problem, while standard graph queries miss the qualitative voice. WikiFM's bipartite fusion proves that **the links between documents must be trained alongside the text of the documents**.

### B. RAG Decay Mitigation
In our earlier work on RAG decay (`HANDOFF_20260804_RAG_Decay_Implementation.md`), we noted that static vector databases decay because semantic distance does not preserve causal history. 
WikiFM solves this by making the relational graph trainable: when an agent repeatedly traverses an epistemic corridor between two files, the GNN weights ($\alpha_{uv}$) can be updated. **This is Epiplexity in silicon:** the graph crystallizes the scar tissue of prior multi-hop reasoning.
