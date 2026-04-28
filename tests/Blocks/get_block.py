"""Example: Retrieve information about a specific block.

This script demonstrates how to fetch details about a block in a Notion page
using its block ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Get the block information and print it
block = notion.get_block(page_id)
print(block)
