# Strategic Planning AI Workspace

This repository hosts a multi-service AI assistant that combines a LangGraph-powered FastAPI agent with a dedicated Retrieval-Augmented Generation (RAG) backend and a pgvector-enabled Postgres database. The stack is packaged for local development via Docker Compose and includes a lightweight UI for end-to-end testing.

---

## 1. System Architecture

The solution is composed of three core services plus supporting infrastructure:

- **Agent API (`services/agent_ai`)**  
  FastAPI application with LangGraph workflows, authentication/session management, rate limiting, Prometheus metrics, and a mock `/ui` console. It calls out to LLM providers (OpenAI or Google Gemini) and the RAG service through the `rag_search` LangGraph tool.

- **RAG API (`services/rag_api`)**  
  FastAPI application responsible for file ingestion, chunking, embedding creation, and vector similarity search. It exposes signed endpoints such as `/embed`, `/query`, and `/ids`. A shared JWT secret protects these endpoints from ad-hoc access.

- **Postgres + pgvector (`db` service)**  
  Stores conversational state (LangGraph checkpoints), user/session records, and vector embeddings in dedicated schemas. The RAG service writes document chunks here; the agent reads them when resolving queries.

- **External Providers**  
  The agent communicates with LLM and embeddings providers (OpenAI/Google) and exports traces/metrics to Prometheus, Grafana, and Langfuse for observability.

Updated diagrams that reflect the current codebase live under `architecture/`:

- `architecture/architecture.puml` : component-level layout of services and integrations  
- `architecture/sequence.puml` : runtime flow from session bootstrap through chat and document ingestion

Render them with `plantuml` if you want PNG/SVG outputs.

---

## 2. Prerequisites

- Docker Engine and Docker Compose plugin (v2+ recommended)
- Python 3.10+ if you plan to run pieces outside containers
- `uv` package manager (optional) for local dependency work
- Valid API keys for any LLM or embedding providers you plan to use (e.g. Google Generative AI)

---

## 3. Environment Configuration

1. **Copy the provided examples**  
   - `services/agent_ai/.env.development` and `services/rag_api/.env` already contain template values. Adjust secrets before running in production.

2. **Align shared secrets**  
   - `RAG_JWT_SECRET` must match `JWT_SECRET` in the RAG service so the agent can authenticate its proxy calls.
   - Keep `COLLECTION_NAME`, `POSTGRES_*`, and API keys consistent between services.

3. **Tune chunking/embedding settings** (optional)  
   - `CHUNK_SIZE`, `CHUNK_OVERLAP`, and `PDF_EXTRACT_IMAGES` live in `services/rag_api/.env` and govern how documents are split.

---

## 4. Running the Stack

1. **Start all services**
   ```bash
   docker compose -f docker_compose.yml up --build
   ```
   This launches:
   - `db` – pgvector-backed Postgres database (exposed on `localhost:55432`)
   - `rag_api` – document ingestion and retrieval service (`http://localhost:8010`)
   - `agent_api` – LangGraph agent API and testing UI (`http://localhost:8000`)

2. **Check health**
   - Agent health: `curl http://localhost:8000/health`
   - RAG docs: open `http://localhost:8010/docs`

3. **Stop services**
   ```bash
   docker compose -f docker_compose.yml down
   ```

---

## 5. Loading Documents into the RAG Store

Use the agent’s document proxy or call the RAG API directly.

### Option A – Browser UI
1. Open `http://localhost:8000/ui`.
2. Register or use anonymous session creation.
3. In the “Knowledge Base” card, choose a `file_id` (e.g. `strategic_docs`) and upload PDFs or text files.
4. Hit “Refresh IDs” to confirm the file was indexed.

### Option B – Scripted Upload
```python
import os
import pathlib

import jwt
import requests

RAG_BASE = "http://localhost:8010"
JWT_SECRET = os.environ["RAG_JWT_SECRET"]
FILE_ID = "university_publications_2024"
FILE_PATH = pathlib.Path("data/university/reports/summary.pdf")

token = jwt.encode({"sub": "agent_service"}, JWT_SECRET, algorithm="HS256")
with FILE_PATH.open("rb") as fh:
    resp = requests.post(
        f"{RAG_BASE}/embed",
        data={"file_id": FILE_ID},
        files={"file": (FILE_PATH.name, fh, "application/pdf")},
        headers={"Authorization": f"Bearer {token}"},
        timeout=180,
    )
resp.raise_for_status()
print(resp.json())
```

### Verification
- `GET http://localhost:8010/ids` – list all stored file identifiers
- `GET http://localhost:8010/documents/{file_id}/context` – inspect chunk summaries
- Update `RAG_DEFAULT_FILE_IDS` in `services/agent_ai/.env.development` to make the agent query those documents by default.

---

## 6. Chatting with the Agent

1. Open `http://localhost:8000/ui` or call the API directly.
2. Create a session with `/api/v1/auth/session` (authentication is optional; a guest user is created automatically).
3. Send conversation payloads to `/api/v1/chatbot/chat` or stream responses from `/api/v1/chatbot/chat/stream`.
4. Use `/api/v1/chatbot/messages` to retrieve or clear the chat history stored in LangGraph checkpoints.

---

## 7. Monitoring & Observability

- Prometheus metrics are exposed by the agent service; Grafana dashboards ship in `services/agent_ai/grafana`.
- Langfuse integration captures traces when `LANGFUSE_*` keys are configured.
- Structured logs follow the Structlog configuration in `services/agent_ai/app/core/logging.py`.

---

## 8. Repository Structure (Highlights)

```
architecture/                Updated PlantUML diagrams
data/                        Example documents to ingest
services/agent_ai/           LangGraph FastAPI agent
  ├── app/                   Source code (APIs, LangGraph, tools)
  ├── Dockerfile             Agent container definition
  └── README.md              Additional agent-specific docs
services/rag_api/            RAG ingestion/search backend
  ├── app/                   FastAPI routes, vector store utilities
  └── Dockerfile             RAG container definition
docker_compose.yml           Orchestrates db, rag_api, agent_api
```

---

## 9. Next Steps

- Extend the ingestion pipeline for scheduled data refreshes (cron or CI job).
- Customize LangGraph tools under `services/agent_ai/app/core/langgraph/tools/` to add new retrieval or reasoning capabilities.
- Export rendered architecture diagrams and embed them into documentation or slide decks.

Feel free to iterate on the environment configuration and chunking parameters as you ingest larger university datasets or private knowledge sources.

