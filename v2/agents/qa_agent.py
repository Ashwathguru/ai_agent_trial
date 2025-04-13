from langchain_openai.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

def generate_test_cases(code: str) -> str:
    prompt = f"""You are a QA engineer. You have been given the following Python function:

{code}

Write 1 positive and 1 negative test case using the unittest module. Return only the test code.
"""
    return llm.predict(prompt).strip()
