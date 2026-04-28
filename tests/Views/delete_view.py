"""Example: Delete a view from a Notion database.

This script demonstrates how to remove a specific view using its view ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

view_id = os.getenv("DEL_VIEW_ID")

# Delete the view and print the response
view = notion.delete_view(view_id)
print(view)
