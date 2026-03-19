from typing import Protocol


class LLMProvider(Protocol):
    def generate(self, prompt: str) -> str: ...


class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return (
            "LLM summary: suspicious activity identified. Recommended next steps include IOC validation, "
            "endpoint isolation, and credential review."
        )
