import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env contents into environment variables

SAP_BASE_URL = os.getenv("SAP_BASE_URL")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
TABLEAU_SITE_ID = os.getenv("TABLEAU_SITE_ID")
TABLEAU_TOKEN = os.getenv("TABLEAU_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
