"""Example: Retrieve all comments from a Notion page or block.

This script demonstrates how to fetch all comments associated with
a specific page or block.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Get all comments and print them
comments = notion.get_all_comments(page_id)
print(comments)
