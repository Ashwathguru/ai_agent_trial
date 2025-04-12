import logging
from config import TABLEAU_SITE_ID

def tableau_filter(query: str) -> str:
    logging.info(f"Simulating Tableau filter for: {query}")
    dashboard_url = f"https://public.tableau.com/views/SampleDashboard?site={TABLEAU_SITE_ID}&filter={query.replace(' ', '+')}"
    result = f"Filtered dashboard link: {dashboard_url}"
    logging.info(f"Simulated Tableau dashboard link: {result}")
    return result
