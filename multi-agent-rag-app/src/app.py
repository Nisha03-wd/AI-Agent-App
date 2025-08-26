import streamlit as st
from coordinator_agent import CoordinatorAgent
from salary_agent import SalaryAgent
from insurance_agent import InsuranceAgent

# Dummy vector store for demonstration
class DummyVectorStore:
    def query(self, question):
        return "Context from vector store"

def main():
    st.title("Multi-Agent RAG System")
    st.write("Ask your questions about salaries or insurance.")

    user_query = st.text_input("Your Question:")

    # Initialize agents and coordinator
    vector_store = DummyVectorStore()
    salary_agent = SalaryAgent(vector_store)
    insurance_agent = InsuranceAgent(vector_store)
    coordinator = CoordinatorAgent(salary_agent, insurance_agent)

    if st.button("Submit"):
        if user_query:
            response = coordinator.handle_query(user_query)
            st.write("Response:", response)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()