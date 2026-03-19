def evaluate_prompt(payload) -> dict:
    score = 50
    feedback = []
    prompt = payload.prompt.lower()

    if "role" in prompt or "you are" in prompt:
        score += 10
    else:
        feedback.append("Add a clear role for the model.")

    if "output" in prompt or "format" in prompt:
        score += 10
    else:
        feedback.append("Specify expected output format.")

    if "do not" in prompt or "only" in prompt:
        score += 10
    else:
        feedback.append("Add boundaries or guardrails.")

    if "context" in prompt or "log" in prompt or "alert" in prompt:
        score += 10
    else:
        feedback.append("Include domain-specific context.")

    if len(payload.prompt) > 120:
        score += 10
    else:
        feedback.append("Provide richer task detail for higher accuracy.")

    return {"score": min(score, 100), "feedback": feedback or ["Prompt is well structured."]}
