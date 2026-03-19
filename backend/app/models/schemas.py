from pydantic import BaseModel, Field
from typing import List, Optional


class LogAnalysisRequest(BaseModel):
    source: str = Field(...)
    raw_log: str = Field(...)


class LogAnalysisResponse(BaseModel):
    summary: str
    llm_summary: str
    severity: str
    risk_score: int
    iocs: List[str]
    attack_patterns: List[str]
    recommendations: List[str]
    analyst_prompt: str


class PlaybookRequest(BaseModel):
    incident_type: str
    context: str


class PromptEvalRequest(BaseModel):
    prompt: str
    use_case: Optional[str] = "security-analysis"


class KnowledgeSearchRequest(BaseModel):
    query: str
