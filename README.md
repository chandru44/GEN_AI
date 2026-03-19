# GenAI Cybersecurity Cloud SOC Copilot v2

Production-oriented portfolio project for **Generative AI + Cybersecurity + Cloud + Prompt Engineering**.

## What changed in v2
- Layered backend architecture
- API key auth middleware
- LLM provider abstraction
- RAG-ready knowledge service
- Structured logging
- Health and readiness endpoints
- Unit tests
- Terraform starter for AWS
- Better config and environment handling
- Safer prompt template structure for security workflows

## Enterprise Use Case
An AI-powered SOC Copilot that helps analysts triage alerts, summarize incidents, generate playbooks, and query internal security knowledge safely.

## Architecture
- **Frontend**: React dashboard for analysts
- **Backend API**: FastAPI with versioned routes
- **AI Layer**: provider abstraction + prompts + RAG-ready retrieval service
- **Security Layer**: IOC extraction, severity scoring, analyst workflows
- **Cloud**: Docker + Terraform starter + GitHub Actions
- **Observability**: structured logs and health checks

## Services
- `/api/v1/analyze-log`
- `/api/v1/generate-playbook`
- `/api/v1/prompt-evaluator`
- `/api/v1/knowledge-search`
- `/health`
- `/ready`

## Production Notes
This repo is designed as a **strong GitHub project** and **production-style starter**, not a finished enterprise SOC platform. To make it fully production-ready, add:
- SSO / JWT auth
- Redis cache / queueing
- Real vector database
- SIEM integrations
- Full audit trails
- RBAC and tenant isolation
