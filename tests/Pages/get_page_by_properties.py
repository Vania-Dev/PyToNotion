"""Example: Retrieve a specific property from a Notion page.

This script demonstrates how to fetch a particular property value
from a page in a Notion database.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_DB_ID")
property = "Food group"  # Name of the property to retrieve

# Get the specific property from the page and print it
page = notion.get_page_by_property(page_id, property)
print(page)
