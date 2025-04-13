from langchain_openai.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

def get_requirement():
    prompt = "Generate a very simple software task that a junior Python developer could complete in a few lines."
    return llm.predict(prompt).strip()
