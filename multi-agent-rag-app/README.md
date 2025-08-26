# Multi-Agent RAG App

This project implements a multi-agent system using LangChain, designed to answer user queries related to salaries and insurance. The system consists of specialized agents that utilize a shared vector store for retrieval-augmented generation (RAG).

## Project Structure

```
multi-agent-rag-app
├── data
│   ├── salary.txt
│   └── insurance.txt
├── src
│   ├── vector_store.py
│   ├── salary_agent.py
│   ├── insurance_agent.py
│   ├── coordinator_agent.py
│   └── app.py
├── requirements.txt
└── README.md
```

## Data Files

- **data/salary.txt**: Contains information about salary structures, including monthly and annual salaries, as well as deductions.
- **data/insurance.txt**: Explains insurance benefits, covering aspects such as coverage, premium, and the claim process.

## Agents

- **SalaryAgent**: This agent specializes in answering salary-related questions. It retrieves relevant information from the vector store to provide accurate answers.
  
- **InsuranceAgent**: This agent focuses on insurance-related queries. It also utilizes the vector store to fetch context and respond to user questions.

- **CoordinatorAgent**: Acts as the main controller of the system. It receives user queries, determines which specialized agent to call, and forwards the query accordingly.

## Application

- **app.py**: The entry point of the application. It sets up the Streamlit interface, handles user input, and displays responses from the Coordinator Agent.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd multi-agent-rag-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage

Once the application is running, you can enter queries related to salaries or insurance. The Coordinator Agent will route your query to the appropriate specialized agent, and you will receive a response based on the information stored in the vector store.

## Example Queries

- **Salary Question**: "How do I calculate annual salary?"
  - **Response**: "Your annual salary is monthly salary × 12, minus deductions."

## By Nisha

