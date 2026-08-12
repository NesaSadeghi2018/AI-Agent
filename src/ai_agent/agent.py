class StrategicIntelligenceAgent:
    def __init__(self, name: str = "Strategic Intelligence Agent"):
        self.name = name

    def analyze(self, question: str) -> str:
        return f"{self.name} received: {question}"