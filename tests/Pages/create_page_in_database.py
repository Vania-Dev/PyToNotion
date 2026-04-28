"""Example: Create a new page inside a Notion database.

This script demonstrates how to create a new entry (page) within a
Notion database with specific property values.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
db_id = os.getenv("DB_ID")

# Define the properties for the new database entry
properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "Name of person"
                    }
                }
            ]
        },
        "Description": {
            "rich_text": [
                {
                    "text": {
                        "content": "Text for test"
                    }
                }
            ]
        }
    }

# Create the page in the database and print the response
page = notion.create_page_in_database(db_id, properties)
print(page)
