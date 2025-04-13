AI Agent-Based Software Workflow (PM → Dev → QA)
===============================================

This project is a simple agent-based Python application using FastAPI. It simulates a software development workflow using three AI-powered agents:

1. Product Manager Agent – Generates simple software requirements.
2. Developer Agent – Writes Python code based on the requirement.
3. QA Agent – Creates positive and negative test cases to test the generated code.

Features
--------

- Individual endpoints for each agent
- Fallback responses if a previous agent hasn't run
- Saves files in separate folders:
  - dev_code/ – stores generated code
  - qa_report/ – stores test cases as Python files
- Automatically deletes old files before saving new ones
- Cleans up code formatting (e.g., removes ```python)

Project Structure
-----------------

.
├── main.py
├── config.py
├── .env
├── dev_code/
│   └── generated_code.py
├── qa_report/
│   └── test_report.py
└── agents/
    ├── product_manager.py
    ├── developer.py
    └── qa_agent.py

Setup Instructions
------------------

1. Clone the repository and enter the project folder.

2. Install dependencies:
   pip install fastapi uvicorn openai python-dotenv

3. Create a .env file with your OpenAI API key:

   OPENAI_API_KEY=your-openai-key-here

4. Start the server:
   uvicorn main:app --reload

API Endpoints (GET)
-------------------

/product_manager - Generates a new software requirement

/developer - Generates Python code for the latest requirement

/qa - Generates test cases for the latest code

/reset - Resets internal memory and deletes generated files

Example Flow (Using curl)
-------------------------

curl http://127.0.0.1:8000/product_manager
curl http://127.0.0.1:8000/developer
curl http://127.0.0.1:8000/qa

Fallback Behavior
-----------------

- /developer before /product_manager → "PM didn’t tell me anything."
- /qa before /product_manager or /developer → "Waiting for Code."
