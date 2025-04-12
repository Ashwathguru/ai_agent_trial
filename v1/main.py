from fastapi import FastAPI, Request
from agent import run_query
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("query")
    logging.info(f"Received query: {question}")
    response = await run_query(question)
    logging.info(f"Response from agent: {response}")
    return {"response": response}
