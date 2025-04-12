import requests
import logging
from config import SAP_BASE_URL

def sap_query(query: str) -> str:
    logging.info(f"Executing mock SAP query: {query}")
    try:
        response = requests.get(f"{SAP_BASE_URL}/products/1")
        response.raise_for_status()
        product = response.json().get("title", "Unknown Product")
        result = f"Product name from dummy SAP: {product}"
    except Exception as e:
        result = f"Error fetching dummy SAP data: {str(e)}"
    logging.info(f"SAP mock result: {result}")
    return result
