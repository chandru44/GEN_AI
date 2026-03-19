# Production-Level Design

## Backend
- FastAPI with versioned APIs
- Auth middleware
- Service/repository separation
- Prompt layer and LLM abstraction
- Input trimming and basic safety controls

## Frontend
- Analyst dashboard
- Future additions: auth, charts, file upload, case timeline

## Cloud
- ECS/App Runner for backend
- S3/CloudFront for frontend
- Secrets Manager for keys
- CloudWatch for logs and metrics
- Terraform for infra baseline

## Security
- API key auth starter
- Future: JWT, RBAC, tenant isolation, audit logging, WAF, rate limits
