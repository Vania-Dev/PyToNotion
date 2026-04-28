"""Example: Create a new page inside another Notion page.

This script demonstrates how to create a child page within an existing
Notion page using the PyToNotion library.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Define the properties for the new page
properties = {
            "title": [
                {
                    "text": {
                        "content": "Test of a create page"
                    }
                }
            ]
        }

# Create the page and print the response
page = notion.create_page(page_id, properties)
print(page)
