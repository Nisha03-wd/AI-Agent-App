class SalaryAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def answer_question(self, question):
        # Retrieve relevant context from the vector store
        context = self.vector_store.query(question)
        
        # Process the context to generate an answer
        if "annual salary" in question.lower():
            return "Your annual salary is monthly salary × 12, minus deductions."
        elif "monthly salary" in question.lower():
            return "Your monthly salary is the total annual salary divided by 12."
        elif "deductions" in question.lower():
            return "Deductions may include taxes, retirement contributions, and health insurance premiums."
        else:
            return "I'm sorry, I can only answer questions related to salaries."