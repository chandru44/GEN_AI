# AWS Deployment Design

## Recommended Architecture
- React frontend on S3 + CloudFront
- FastAPI backend on ECS Fargate or App Runner
- Logs and audit data in CloudWatch + S3
- Secrets in AWS Secrets Manager
- Optional vector search in OpenSearch / pgvector
- CI/CD through GitHub Actions

## Security Considerations
- IAM least privilege
- WAF in front of public endpoints
- API throttling and auth
- KMS encryption for secrets and storage
- VPC-private backend for enterprise mode
