"""Example: Retrieve a Notion page by its ID.

This script demonstrates how to fetch information about a specific
Notion page using its unique identifier.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

# Get the page ID from environment variables
page_id = os.getenv("PAGE_ID")

# Retrieve the page information and print it
page = notion.get_page(page_id)
print(page)
