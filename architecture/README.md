# Architecture Diagrams

This directory contains the architecture documentation for the Strategic Planning AI system, organized hierarchically for easy navigation.

## 📁 Diagram Organization

Files use a hierarchical numbering system:
- **xx** = Layer number (01, 10, 20, 30, etc.)
- **xx_yy** = Component within that layer

### 🌐 High-Level Overview (01-02)
Start here to understand the overall system architecture.

| File | Description |
|------|-------------|
| `01_overview_simplified` | **Simplified system overview** - Best starting point, shows major layers |
| `02_overview_detailed` | **Detailed architecture** - Complete system view with all components |

---

### 🔷 Layer 10: Client Layer
User-facing components and external integrations.

| File | Description |
|------|-------------|
| `10_layer_client` | **Client Layer** - User interfaces, web dashboard, external integrations |

---

### 🔷 Layer 20: Service Layer (Microservices)
Core business logic microservices - one overview + details for each service.

| File | Description |
|------|-------------|
| `20_layer_service_microservices` | **Microservices Overview** - Compact view of all 3 services |
| `20_01_component_agent_service` | **Agent Service Detail** - LangGraph orchestration, APIs, tools |
| `20_02_component_rag_service` | **RAG Service Detail** - Document processing, vector + graph storage |
| `20_03_component_analysis_service` | **Analysis Service Detail** - Strategic workflows, rules, scenarios |

---

### 🔷 Layer 30: Knowledge/Data Layer
Data storage and knowledge management.

| File | Description |
|------|-------------|
| `30_layer_knowledge_data` | **Knowledge Layer Overview** - Vector store + knowledge graph architecture |
| `30_01_component_ingestion_pipeline` | **Data Ingestion Pipeline** - Step-by-step document processing (14 steps) |
| `30_02_component_neo4j_graph` | **Neo4j Knowledge Graph** - Graph schema, operations, queries |

---

### 🔄 Other Diagrams (40+)

| File | Description |
|------|-------------|
| `40_sequence_runtime_flows` | **Runtime Sequences** - Key runtime flows: session, ingestion, chat |

---

## 🎯 Quick Navigation Guide

### 📍 **"I want to understand the overall system"**
→ Start with: `01_overview_simplified`

### 📍 **"I need to see all components and connections"**
→ Look at: `02_overview_detailed`

### 📍 **"I'm implementing the microservices"**
→ Start: `20_layer_service_microservices` (overview)
→ Then: `20_01` (Agent), `20_02` (RAG), `20_03` (Analysis)

### 📍 **"I'm working on document processing"**
→ Study: `30_01_component_ingestion_pipeline` and `30_layer_knowledge_data`

### 📍 **"I need to understand the knowledge graph"**
→ See: `30_02_component_neo4j_graph`

### 📍 **"I want to trace a user request flow"**
→ Follow: `40_sequence_runtime_flows`

---

## 🏗️ Architecture Layers

```
┌─────────────────────────────────────────┐
│   Layer 10: Client Layer                │  Web UI, External Consumers
├─────────────────────────────────────────┤
│   Layer 20: Service Layer               │  Microservices:
│   ├─ 20_01: Agent Service (8000)        │  - Main orchestration
│   ├─ 20_02: RAG Service (8080)          │  - Document processing  
│   └─ 20_03: Analysis Service (8090)     │  - Strategic workflows
├─────────────────────────────────────────┤
│   Layer 30: Knowledge/Data Layer        │  Storage:
│   ├─ 30_01: Ingestion Pipeline          │  - Document processing
│   └─ 30_02: Neo4j Knowledge Graph       │  - Entity relationships
│                                         │  - Vector Store (pgvector)
└─────────────────────────────────────────┘
```

---

## 🛠️ Generating Diagrams

To regenerate PNG images from PlantUML source files:

```bash
# Generate all diagrams
java -jar plantuml.jar -tpng *.puml

# Generate specific diagram
java -jar plantuml.jar -tpng 01_overview_simplified.puml

# Generate high-level diagrams only
java -jar plantuml.jar -tpng 01_overview_*.puml 02_overview_*.puml
```

---

## 📋 File Naming Convention

```
Hierarchical numbering:
  xx              = Layer number (e.g., 10, 20, 30)
  xx_yy           = Component within that layer
  
Examples:
  01              = Overview level
  10              = Client layer
  20              = Service layer
  20_01           = Component within service layer (microservices detail)
  20_02           = Another component within service layer (analysis)
  30              = Knowledge/data layer
  30_01           = Component within knowledge layer (ingestion)
  30_02           = Another component (Neo4j)
  40+             = Other diagrams (sequences, etc.)
```

### Categories in Names:
- **overview** - High-level system views (01-02)
- **layer** - Architectural layer (10, 20, 30)
- **component** - Specific component within a layer (xx_yy)
- **sequence** - Runtime sequence diagrams (40+)

---

## 🎨 Diagram Standards

All diagrams follow these conventions:
- **No colored backgrounds** - Clean, document-ready
- **Black borders (1px)** - Professional appearance
- **Arial font (11pt)** - Readable in documents
- **Clear labels** - Descriptive names and annotations
- **Notes sections** - Key information highlighted

---

## 📊 Technology Stack Shown

### Services
- **Agent Service**: FastAPI, LangGraph, SQLModel
- **RAG Service**: FastAPI, LangChain, pgvector, Neo4j
- **Analysis Service**: FastAPI, Celery, Ray, Redis

### Data Storage
- **Postgres + pgvector**: Vector embeddings, sessions, state
- **Neo4j**: Knowledge graph (entities, relationships)
- **Redis**: Task queue, caching

### External Services
- **OpenAI**: LLM completions, embeddings
- **Prometheus**: Metrics collection
- **Grafana**: Metrics visualization
- **Langfuse**: LLM tracing

---

## 🔄 Update Process

When updating architecture:
1. Edit the `.puml` source file
2. Regenerate PNG: `java -jar plantuml.jar -tpng [filename].puml`
3. Verify the output looks correct
4. Update this README if adding new diagrams

---

## 📚 Related Documentation

- `/MICROSERVICES_OVERVIEW.md` - Detailed microservices documentation
- `/README.md` - Project README
- `/services/agent_ai/README.md` - Agent service documentation
- `/services/rag_api/README.md` - RAG service documentation

---

## 🏆 Best Practices

1. **Start High-Level** - Begin with overview diagrams
2. **Drill Down** - Move to layer and component details
3. **Follow Sequences** - Use sequence diagrams to understand flows
4. **Cross-Reference** - Use multiple diagrams for complete understanding
5. **Keep Updated** - Update diagrams when architecture changes

---

**Last Updated**: 2025-10-29
**Architecture Version**: 1.0
**Maintained By**: Strategic Planning AI Team
