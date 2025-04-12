import pandas as pd
import logging
import os

try:
    import duckdb
    DUCKDB_AVAILABLE = True
except ImportError:
    DUCKDB_AVAILABLE = False
    logging.warning("DuckDB not available. Falling back to head(3) mode.")

def bigquery_query(query: str) -> str:
    logging.info(f"Executing pseudo BigQuery SQL: {query}")
    csv_path = "data/sales.csv"

    if not os.path.exists(csv_path):
        msg = f"CSV file not found at path: {csv_path}"
        logging.error(msg)
        return msg

    try:
        if DUCKDB_AVAILABLE:
            con = duckdb.connect()
            con.execute(f"CREATE OR REPLACE VIEW sales_table AS SELECT * FROM read_csv_auto('{csv_path}')")
            result_df = con.execute(query).fetchdf()
        else:
            df = pd.read_csv(csv_path)
            result_df = df.head(3)
        result = result_df.to_string(index=False)
    except Exception as e:
        result = f"Error processing query: {str(e)}"

    logging.info(f"Simulated BigQuery result: {result}")
    return result
