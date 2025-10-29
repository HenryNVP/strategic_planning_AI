# Architecture Files Index

## Complete File List (Sorted by Hierarchy)

### Overview Level
- `01_overview_simplified.{puml,png}` - High-level system overview
- `02_overview_detailed.{puml,png}` - Detailed architecture with all components

### Layer 10: Client
- `10_layer_client.{puml,png}` - Client layer (UI, integrations)

### Layer 20: Service (Microservices)
- `20_layer_service_microservices.{puml,png}` - Service layer overview
- `20_01_component_microservices_detail.{puml,png}` - Microservices detailed breakdown
- `20_02_component_analysis_service.{puml,png}` - Analysis service component

### Layer 30: Knowledge/Data
- `30_layer_knowledge_data.{puml,png}` - Knowledge layer overview
- `30_01_component_ingestion_pipeline.{puml,png}` - Data ingestion pipeline
- `30_02_component_neo4j_graph.{puml,png}` - Neo4j knowledge graph

### Other (40+)
- `40_sequence_runtime_flows.{puml,png}` - Runtime sequence diagrams

---

## Naming Convention

```
Format: XX[_YY]_category_description

Where:
  XX    = Layer number (01=overview, 10=client, 20=service, 30=knowledge, 40+=other)
  YY    = Component number within layer (optional)
  
Examples:
  01_overview_simplified              → Overview level
  20_layer_service_microservices      → Layer 20 overview
  20_01_component_microservices_detail → Component 01 within layer 20
  20_02_component_analysis_service    → Component 02 within layer 20
```

## Quick Reference

**Start Here:** `01_overview_simplified`

**Layers:**
- 10 = Client
- 20 = Service (Microservices)
- 30 = Knowledge/Data

**Components:** Use `XX_YY` format (e.g., `20_01`, `30_01`)
