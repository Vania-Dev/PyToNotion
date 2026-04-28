"""Example: Create a new view in a Notion database.

This script demonstrates how to create a table view with specific
property configurations for a database.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
db_id = os.getenv("DB_ID")
ds_id = os.getenv("DATASOURCE_ID")

# Define the view configuration
data = {
    "data_source_id": ds_id,
    "name": "Fruits Only test",
    "type": "table",
    "database_id": db_id,
    # Specific configuration for the view
    "configuration": {
        "type": "table",
        "title": "Test form",
        "properties": [
            {
                "property_id": "title",
                "visible": True,
                "required": True
            },
            {
                "property_id": "w%3Fj_",
                "visible": True
            },
            {
                "property_id": "kB~w",
                "visible": True
            },
            {
                "property_id": "%3D~ay",
                "visible": True
            },
            {
                "property_id": "d_%5Bk",
                "visible": True
            },
            {
                "property_id": "ZQ_V",
                "visible": True
            },
            {
                "property_id": "mrPB",
                "visible": True
            },
            {
                "property_id": "f~m_",
                "visible": True
            }
        ]
    }
}

# Create the view and print the response
view = notion.create_view(data)
print(view)
