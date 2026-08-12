from ai_agent.agent import StrategicIntelligenceAgent
from ai_agent.mock_llm import MockLLM


def main():
    llm = MockLLM()
    agent = StrategicIntelligenceAgent(llm)

    question = "What are the main drivers of declining sales?"

    response = agent.analyze(question)

    print(response)


if __name__ == "__main__":
    main()