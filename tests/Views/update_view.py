"""Example: Update an existing view in a Notion database.

This script demonstrates how to modify view properties such as name,
type, and property configurations.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
view_id = os.getenv("FORM_VIEW_ID")

# Define the updated view configuration
data = {
    "name": "Form",
    "type": "table",
    "title": "Test form",
    # Specific configuration for the view
    "configuration": {
        "type": "table",
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

# Update the view and print the response
view = notion.update_view(view_id, data)
print(view)
