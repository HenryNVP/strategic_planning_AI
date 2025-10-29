# Architecture Clarification

## ❓ Common Questions Answered

### Q: Does the ingestion pipeline belong to the Knowledge Layer (Layer 3)?

**A: NO.** The ingestion pipeline is **part of the RAG Service (Layer 2)**, not the Knowledge/Data Layer (Layer 3).

## 📐 Layer Responsibilities

### **Layer 2: Service Layer** (Processing)
**What happens here:**
- **RAG Service** performs document ingestion:
  - Loads documents (PDF, CSV, DOCX, etc.)
  - Extracts and cleans text
  - Chunks documents
  - Generates embeddings (via OpenAI)
  - Extracts entities (NER)
  - **Writes data to Layer 3**

**Diagram:** `A2_02_component_rag_service.puml` shows RAG Service components

### **Layer 3: Knowledge/Data Layer** (Storage)
**What happens here:**
- **Postgres**: Stores 3 types of data
  - Application data (users, sessions, checkpoints)
  - University domain data (courses, students, faculty, budgets)
  - Vector store (pgvector: document chunks + embeddings)
- **Neo4j**: Stores graph data
  - Entity nodes (people, concepts, strategies)
  - Relationships (edges with properties)

**Diagram:** `A3_layer_knowledge_data.puml` shows storage components

### **Layer 4: Flows & Sequences** (How it works)
**What happens here:**
- Shows **how services interact**
- Shows **data flows between layers**
- **A4_01_flow_ingestion_pipeline.puml**: Shows the complete document processing flow
  - Starts: Client uploads to Agent Service
  - Middle: RAG Service processes (Layer 2)
  - End: Data stored in Postgres + Neo4j (Layer 3)

## 🔄 Document Ingestion Flow Summary

```
CLIENT (Layer 1)
    ↓ upload document
AGENT SERVICE (Layer 2)
    ↓ proxy to RAG
RAG SERVICE (Layer 2) ← Does ALL processing:
    ├─ Load file
    ├─ Extract text
    ├─ Clean text
    ├─ Chunk text
    ├─ Generate embeddings (OpenAI)
    ├─ Extract entities (NER)
    └─ Write to storage ↓
         ↓
STORAGE (Layer 3) ← Only receives data:
    ├─ Postgres (pgvector): chunks + vectors
    └─ Neo4j: entities + relationships
```

## 📊 Diagram Reference

| Question | Which Diagram? |
|----------|----------------|
| "What does RAG Service do?" | `A2_02_component_rag_service.puml` |
| "How does document ingestion work?" | `A4_01_flow_ingestion_pipeline.puml` |
| "What's stored in Layer 3?" | `A3_layer_knowledge_data.puml` |
| "What's the full architecture?" | `A0_02_overview_detailed.puml` |

## 🎯 Key Takeaway

**Processing vs. Storage:**
- **Layer 2 (Services)** = Active processing, business logic
- **Layer 3 (Storage)** = Passive data storage, no logic
- **Layer 4 (Flows)** = Documentation of how layers interact

**The RAG Service (Layer 2) owns the ingestion pipeline.**
**Layer 3 only provides storage for the results.**

---

**Last Updated**: 2025-10-29

