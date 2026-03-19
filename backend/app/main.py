from fastapi import FastAPI
from app.api.routes import router
from app.core.logging_config import setup_logging
from app.core.config import settings

setup_logging()
app = FastAPI(title="GenAI Cybersecurity Cloud SOC Copilot v2", version="2.0.0")
app.include_router(router, prefix="/api/v1")

@app.get('/health')
def health() -> dict:
    return {'status': 'ok', 'service': settings.app_name}

@app.get('/ready')
def ready() -> dict:
    return {'status': 'ready', 'env': settings.app_env}
