"""Example: Create a new datasource in a Notion database.

This script demonstrates how to create a datasource with custom properties
for managing data in a Notion database.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
db_id = os.getenv("DB_ID")

# Define the datasource structure with properties
data = {
    "parent": {
        "type": "database_id",
        "database_id": db_id
    },
    "properties": {
        "Name": { "title": {} },
        "Description": { "rich_text": {} },
        "In stock": { "checkbox": {} },
        "Food group": {
            "select": {
                "options": [
                    { "name": "🥦Vegetable", "color": "green" },
                    { "name": "🍎Fruit", "color": "red" },
                    { "name": "💪Protein", "color": "yellow" }
                ]
            }
        },
        "Price": {
            "number": { "format": "dollar" }
        },
        "Last ordered": { "date": {} },
        "Store availability": {
            "multi_select": {
                "options": [
                    { "name": "Duc Loi Market", "color": "blue" },
                    { "name": "Rainbow Grocery", "color": "gray" },
                    { "name": "Nijiya Market", "color": "purple" },
                    { "name": "Gus's Community Market", "color": "yellow" }
                ]
            }
        },
        "+1": { "people": {} },
        "Photo": { "files": {} }
    }
}

# Create the datasource and print the response
database = notion.create_datasource(data)
print(database)
