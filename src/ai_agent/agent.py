from ai_agent.llm import LLMClient


class StrategicIntelligenceAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def analyze(self, question: str) -> str:
        prompt = f"""
You are a strategic intelligence analyst.

Analyze the following business question:

{question}
"""

        return self.llm.generate(prompt)