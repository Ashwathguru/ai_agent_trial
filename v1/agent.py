from langchain.agents import initialize_agent, Tool
from langchain_openai.chat_models import ChatOpenAI
from tools.sap_tool import sap_query
from tools.bq_tool import bigquery_query
from tools.tableau_tool import tableau_filter
from config import OPENAI_API_KEY
import logging
import asyncio
import os

logging.basicConfig(level=logging.INFO)

# Ensure OpenAI API key is set in environment
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(temperature=0)

TOOLS = [
    Tool(name="SAPQuery", func=sap_query, description="Used for querying SAP data"),
    Tool(name="BigQuerySQL", func=bigquery_query, description="Used for running SQL on BigQuery"),
    Tool(name="TableauFilter", func=tableau_filter, description="Used for filtering Tableau dashboards")
]

agent = initialize_agent(TOOLS, llm, agent="zero-shot-react-description", verbose=True)

async def run_query(query: str):
    logging.info(f"Running agent with query: {query}")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, agent.run, query)
    logging.info(f"Agent result: {result}")
    return result
