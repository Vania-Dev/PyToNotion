"""Example: Create a new database in a Notion page.

This script demonstrates how to create a database with custom properties
including title, rich text, checkbox, select, number, date, multi-select,
and file properties.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Define the database structure with properties
data = {
    "parent": {
        "type": "page_id",
        "page_id": page_id
    },
    "title": [
        {"text": {"content": "Grocery List"}}
    ],
    "initial_data_source": {
        "properties": {
            "Name": {"title": {}},
            "Description": {"rich_text": {}},
            "In stock": {"checkbox": {}},
            "Food group": {
                "select": {
                    "options": [
                        {"name": "🥦Vegetable", "color": "green"},
                        {"name": "🍎Fruit", "color": "red"},
                        {"name": "💪Protein", "color": "yellow"}
                    ]
                }
            },
            "Price": {
                "number": {"format": "dollar"}
            },
            "Last ordered": {"date": {}},
            "Store availability": {
                "multi_select": {
                    "options": [
                        {"name": "Duc Loi Market", "color": "blue"},
                        {"name": "Rainbow Grocery", "color": "gray"},
                        {"name": "Nijiya Market", "color": "purple"},
                        {"name": "Gus's Community Market", "color": "yellow"}
                    ]
                }
            },
            "Photo": {"files": {}}
        }
    }
}

# Create the database and print the response
database = notion.create_database(data)
print(database)
