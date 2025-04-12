Initial version of ai agent trial
To run on local, 
Install dependencies from requirement.txt

create a .env file with the following params: 
# This file contains environment variables for the project.
SAP_BASE_URL = "https://dummyjson.com"
GCP_PROJECT_ID = "free-simulated-project"
TABLEAU_SITE_ID = "public-site"
TABLEAU_TOKEN = "dummy-token"
OPENAI_API_KEY = "YOUR_API_KEY"

use uvicorn main:app --reload to start the API

Sample Curl commands that worked: 
curl --location 'http://127.0.0.1:8000/ask' \
--header 'Content-Type: application/json' \
--data '{"query":"Get sales info of Alice from BigQuery","variables":{}}'

curl --location 'http://127.0.0.1:8000/ask' \
--header 'Content-Type: application/json' \
--data '{"query":"Get sales info from BigQuery","variables":{}}'

curl --location 'http://127.0.0.1:8000/ask' \
--header 'Content-Type: application/json' \
--data '{"query":"Get product info from SAP","variables":{}}'