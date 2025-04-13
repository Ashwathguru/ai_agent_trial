from langchain_openai.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

def generate_code(requirement: str) -> str:
    prompt = f"""You are a software developer. Based on the following requirement, write a simple Python function:

Requirement: {requirement}

Only return the Python code without explanation.
"""
    return llm.predict(prompt).strip()
