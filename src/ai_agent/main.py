from ai_agent.agent import StrategicIntelligenceAgent


def main():
    agent = StrategicIntelligenceAgent()

    question = "What are the main drivers of declining sales?"

    response = agent.analyze(question)

    print(response)


if __name__ == "__main__":
    main()