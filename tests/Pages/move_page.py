"""Example: Move a Notion page to a different parent page.

This script demonstrates how to relocate a page within the Notion
workspace by changing its parent.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
move_page_id = os.getenv("MOVE_PAGE_ID")  # Page to be moved
static_page_id = os.getenv("STATIC_PAGE_ID")  # New parent page

# Define the new parent for the page
content = {
    "parent": {
        "page_id": static_page_id,
        "type": "page_id"
    }
}

# Move the page and print the response
page = notion.move_page(move_page_id, content)
print(page)
