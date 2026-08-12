from ai_agent.llm import LLMClient


class MockLLM(LLMClient):
    def generate(self, prompt: str) -> str:
        return f"Mock LLM response to: {prompt}"