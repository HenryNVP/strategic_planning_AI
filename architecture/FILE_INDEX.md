# Architecture Files Index

## Complete File List (Sorted by Hierarchy)

### Overview Level (Layer 0)
- `A0_01_overview_simplified.{puml,png}` - High-level system overview
- `A0_02_overview_detailed.{puml,png}` - Detailed architecture with all components

### Layer 1: Client
- `A1_layer_client.{puml,png}` - Client layer (UI, integrations)

### Layer 2: Service (Microservices)
- `A2_layer_service_microservices.{puml,png}` - Compact overview of all 3 microservices
- `A2_01_component_agent_service.{puml,png}` - Agent service detailed components
- `A2_02_component_rag_service.{puml,png}` - RAG service detailed components
- `A2_03_component_analysis_service.{puml,png}` - Analysis service detailed components

### Layer 3: Knowledge/Data (Storage Only)
- `A3_layer_knowledge_data.{puml,png}` - Storage overview (Postgres + Neo4j)
- `A3_01_component_neo4j_graph.{puml,png}` - Neo4j knowledge graph
- `A3_02_component_university_database.{puml,png}` - University database schema

### Layer 4: Flows & Sequences (Simplified)
- `A4_00_flow_overview.{puml,png}` - Overview (all flows combined, detailed)
- `A4_01_flow_ingestion.{puml,png}` - Document upload (user → storage)
- `A4_02_flow_session_auth.{puml,png}` - Session & auth (login, JWT, logout)
- `A4_03_flow_chat.{puml,png}` - Chat (sync, streaming, history all-in-one)
- `A4_04_flow_analysis.{puml,png}` - Analysis workflow (simplified)

**Detailed versions available in:** `_detailed_backup/` folder

---

## Naming Convention

```
Format: AX[_YY]_category_description

Where:
  X     = Layer number (0=overview, 1=client, 2=service, 3=knowledge, 4+=other)
  YY    = Component number within layer (optional)
  
Examples:
  A0_01_overview_simplified              → Overview level (simplified)
  A0_02_overview_detailed                → Overview level (detailed)
  A1_layer_client                        → Layer 1 (client)
  A2_layer_service_microservices         → Layer 2 overview
  A2_01_component_agent_service          → Component 01 within layer 2
  A2_02_component_rag_service            → Component 02 within layer 2
  A2_03_component_analysis_service       → Component 03 within layer 2
  A3_layer_knowledge_data                → Layer 3 overview (storage)
  A3_01_component_neo4j_graph            → Component 01 within layer 3
  A3_02_component_university_database    → Component 02 within layer 3
  A4_00_flow_overview                    → Overview (all flows)
  A4_01_flow_ingestion_pipeline          → Document ingestion (Layer 2 → Layer 3)
  A4_02_flow_session_auth                → Session & authentication
  A4_03_flow_chat_rag                    → Chat with RAG context
  A4_04_flow_analysis_workflow           → Strategic analysis workflow
```

## Quick Reference

**Start Here:** `A0_01_overview_simplified`

**Layers:**
- 0 = Overview
- 1 = Client
- 2 = Service (Microservices)
- 3 = Knowledge/Data
- 4+ = Sequences & Other

**Components:** Use `AX_YY` format (e.g., `A2_01`, `A3_01`)
