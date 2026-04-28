"""Example: Update properties of an existing Notion database.

This script demonstrates how to modify database properties such as
the title of the database.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
database_id = os.getenv("DB_ID")

# Define the updated database properties
query = {
    "title": [
        {
            "text": {
                "content": "Grocery List Test"
            }
        }
    ]
}

# Update the database and print the response
database = notion.update_database(database_id, query)
print(database)
