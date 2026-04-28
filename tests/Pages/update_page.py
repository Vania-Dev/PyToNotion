"""Example: Update properties of an existing Notion page.

This script demonstrates how to modify the title and other properties
of a Notion page.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Define the updated content for the page
content = {
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": "Notion API :D"
                        }
                    }
                ]
            }
        }
    }

# Update the page and print the response
page = notion.update_page(page_id, content)
print(page)
