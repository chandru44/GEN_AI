def generate_playbook(payload) -> dict:
    steps = [
        f"Identify the affected systems related to {payload.incident_type}.",
        "Collect logs, alerts, user activity, and network telemetry.",
        "Contain the threat by isolating systems or disabling compromised accounts.",
        "Eradicate malicious artifacts and patch exposed vulnerabilities.",
        "Recover systems and monitor for reinfection or persistence.",
        "Document lessons learned and update detections.",
    ]
    return {
        "incident_type": payload.incident_type,
        "context": payload.context,
        "playbook": steps,
    }
