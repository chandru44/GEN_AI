from fastapi import APIRouter, Depends
from app.middleware.auth import verify_api_key
from app.models.schemas import LogAnalysisRequest, LogAnalysisResponse, PlaybookRequest, PromptEvalRequest, KnowledgeSearchRequest
from app.services.log_analyzer import analyze_security_log
from app.services.playbook_generator import generate_playbook
from app.services.prompt_evaluator import evaluate_prompt
from app.services.knowledge_service import search_knowledge

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.post('/analyze-log', response_model=LogAnalysisResponse)
def analyze_log(payload: LogAnalysisRequest) -> LogAnalysisResponse:
    return analyze_security_log(payload)

@router.post('/generate-playbook')
def playbook(payload: PlaybookRequest) -> dict:
    return generate_playbook(payload)

@router.post('/prompt-evaluator')
def prompt_eval(payload: PromptEvalRequest) -> dict:
    return evaluate_prompt(payload)

@router.post('/knowledge-search')
def knowledge_search(payload: KnowledgeSearchRequest) -> dict:
    return search_knowledge(payload.query)
