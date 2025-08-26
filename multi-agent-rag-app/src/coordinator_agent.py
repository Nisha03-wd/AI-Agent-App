class CoordinatorAgent:
    def __init__(self, salary_agent, insurance_agent):
        self.salary_agent = salary_agent
        self.insurance_agent = insurance_agent

    def handle_query(self, query):
        if "salary" in query.lower():
            return self.salary_agent.answer_question(query)
        elif "insurance" in query.lower():
            return self.insurance_agent.answer_question(query)
        else:
            return "Sorry, I can only answer questions about salary or insurance."