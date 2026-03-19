from app.models.schemas import LogAnalysisRequest
from app.services.log_analyzer import analyze_security_log


def test_analyze_security_log():
    payload = LogAnalysisRequest(source="EDR", raw_log="Failed login from 10.0.0.8 then PowerShell execution")
    result = analyze_security_log(payload)
    assert result.severity in ["Medium", "High", "Low"]
    assert isinstance(result.iocs, list)
    assert result.risk_score >= 0
