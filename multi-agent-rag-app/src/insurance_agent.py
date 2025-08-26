class InsuranceAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def answer_question(self, question):
        # Retrieve relevant context from the vector store
        context = self.vector_store.query(question)
        
        # Process the context to generate a response
        if context:
            return f"Insurance Information: {context}"
        else:
            return "I'm sorry, I couldn't find any information related to your insurance question."