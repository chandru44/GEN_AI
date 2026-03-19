import re
from app.models.schemas import LogAnalysisRequest, LogAnalysisResponse
from app.clients.llm_client import MockLLMClient
from app.utils.security import safe_trim

IP_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
CVE_REGEX = r"CVE-\d{4}-\d{4,7}"
DOMAIN_REGEX = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"


def extract_iocs(text: str) -> list[str]:
    iocs = set(re.findall(IP_REGEX, text))
    iocs.update(re.findall(CVE_REGEX, text, flags=re.IGNORECASE))
    iocs.update(re.findall(DOMAIN_REGEX, text))
    return sorted(iocs)


def infer_attack_patterns(text: str) -> list[str]:
    lowered = text.lower()
    patterns = []
    mapping = {
        "Credential Access / Brute Force": ["failed login", "brute force"],
        "Suspicious Script Execution": ["powershell", "encodedcommand"],
        "Possible Data Exfiltration": ["exfiltration", "large outbound"],
        "Possible Ransomware Activity": ["ransom", "encryption"],
    }
    for label, triggers in mapping.items():
        if any(t in lowered for t in triggers):
            patterns.append(label)
    return patterns or ["General Suspicious Activity"]


def score_risk(text: str, iocs: list[str], patterns: list[str]) -> tuple[int, str]:
    score = min(100, 25 + len(iocs) * 8 + len(patterns) * 14)
    if any(k in text.lower() for k in ["admin", "domain controller", "privilege escalation", "critical"]):
        score = min(100, score + 12)
    severity = "Low" if score < 40 else "Medium" if score < 70 else "High"
    return score, severity


def build_prompt(log_text: str) -> str:
    trimmed = safe_trim(log_text)
    return (
        "You are a senior SOC analyst. Analyze the following security event. "
        "Return a concise incident summary, likely threat category, MITRE ATT&CK mapping, top IOCs, "
        "containment actions, and false-positive considerations. Keep it structured.\n\n"
        f"SECURITY_EVENT:\n{trimmed}"
    )


def analyze_security_log(payload: LogAnalysisRequest) -> LogAnalysisResponse:
    iocs = extract_iocs(payload.raw_log)
    patterns = infer_attack_patterns(payload.raw_log)
    risk_score, severity = score_risk(payload.raw_log, iocs, patterns)
    analyst_prompt = build_prompt(payload.raw_log)
    llm_summary = MockLLMClient().generate(analyst_prompt)

    return LogAnalysisResponse(
        summary=f"{payload.source} reported {', '.join(patterns).lower()} with {len(iocs)} indicators extracted.",
        llm_summary=llm_summary,
        severity=severity,
        risk_score=risk_score,
        iocs=iocs,
        attack_patterns=patterns,
        recommendations=[
            "Validate IOC reputation and asset criticality.",
            "Isolate impacted hosts or disable compromised identities.",
            "Review EDR, DNS, proxy, and IAM logs for spread.",
            "Block confirmed malicious indicators and tune detections.",
        ],
        analyst_prompt=analyst_prompt,
    )
