import os
import json
import uuid
from fastapi import FastAPI
from agents.product_manager import get_requirement
from agents.developer import generate_code
from agents.qa_agent import generate_test_cases

app = FastAPI()

latest_requirement = None
latest_code = None

DEV_FOLDER = "dev_code"
QA_FOLDER = "qa_report"

os.makedirs(DEV_FOLDER, exist_ok=True)
os.makedirs(QA_FOLDER, exist_ok=True)

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def clean_code(code: str) -> str:
    """Clean the code to remove unwanted parts like ```python."""
    lines = code.split("\n")
    cleaned_lines = []
    for line in lines:
        # Remove any lines with ```python or ``` 
        if line.strip() and (line.strip() != "```python" and line.strip() != "```"):
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

@app.get("/product_manager")
def call_pm():
    global latest_requirement
    latest_requirement = get_requirement()
    return {"requirement": latest_requirement}

@app.get("/developer")
def call_dev():
    global latest_requirement, latest_code
    if not latest_requirement:
        return {"error": "PM didn’t tell me anything."}
    
    latest_code = generate_code(latest_requirement)
    
    # Clean the code before saving
    cleaned_code = clean_code(latest_code)

    # Save Python code to file
    clear_folder(DEV_FOLDER)
    code_file_path = os.path.join(DEV_FOLDER, "generated_code.py")
    with open(code_file_path, "w") as f:
        f.write(cleaned_code)

    return {
        "generated_code": code_file_path
    }

@app.get("/qa")
def call_qa():
    global latest_code
    if not latest_code:
        return {"error": "Waiting for Code."}
    
    raw_tests = generate_test_cases(latest_code)

    # Clean the code by removing triple backticks
    def clean_test_code(code: str) -> str:
        lines = code.split("\n")
        cleaned = [line for line in lines if line.strip() and line.strip() not in ("```python", "```")]
        return "\n".join(cleaned)

    cleaned_tests = clean_test_code(raw_tests)

    # Inject simple comments for positive and negative tests
    if "Positive test case:" in cleaned_tests:
        cleaned_tests = cleaned_tests.replace("Positive test case:", "#Positive test case:")
    if "Negative test case:" in cleaned_tests:
        cleaned_tests = cleaned_tests.replace("Negative test case:", "#Negative test case:")

    # Save test code to a .py file
    clear_folder(QA_FOLDER)
    test_file_path = os.path.join(QA_FOLDER, "test_report.py")
    with open(test_file_path, "w") as f:
        f.write(cleaned_tests)

    return {
       "generated_test_script": test_file_path
    }


@app.get("/reset")
def reset_state():
    global latest_requirement, latest_code
    latest_requirement = None
    latest_code = None
    clear_folder(DEV_FOLDER)
    clear_folder(QA_FOLDER)
    return {"status": "Session reset. All data cleared."}
