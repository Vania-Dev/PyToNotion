"""Example: Update properties of an existing datasource.

This script demonstrates how to add or modify properties in a datasource,
such as adding a new select property.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
datasource_id = os.getenv("DATASOURCE_ID")

# Define the updated properties for the datasource
data = {
    "properties": {
        "Food group 2": {
            "select": {
                "options": [
                    {"name": "🥦Vegetable", "color": "green"},
                    {"name": "🍎Fruit", "color": "red"},
                    {"name": "💪Protein", "color": "yellow"}
                ]
            }
        }
    }
}

# Update the datasource and print the response
datasource = notion.update_datasource(datasource_id, data)
print(datasource)
