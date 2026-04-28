"""Example: Query a datasource with filters and sorting.

This script demonstrates how to query a datasource with specific filters
(e.g., filtering by select property) and sorting options.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
datasource_id = os.getenv("DATASOURCE_ID")

# Define the query with filter and sort parameters
query = {
    "filter": {
        "property": "Food group",   # Name of your select column
        "select": {
            "equals": "🥦Vegetable"    # Value to filter by
        }
    },
    "sorts": [
        {
            "property": "Name",
            "direction": "ascending"
        }
    ]
}

# Query the datasource and print the results
database = notion.query_datasource(datasource_id, query)
print(database)
