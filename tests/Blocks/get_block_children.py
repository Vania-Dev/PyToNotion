"""Example: Retrieve all child blocks from a Notion page or block.

This script demonstrates how to fetch all blocks that are children
of a specific page or block.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Get all child blocks and print them
block = notion.get_block_children(page_id)
print(block)
