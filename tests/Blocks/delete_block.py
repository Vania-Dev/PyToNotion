"""Example: Delete a block from a Notion page.

This script demonstrates how to remove a specific block from a Notion page
using its block ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

# Get the block ID to delete
block = os.getenv("BLOCK_DEL_ID")

# Delete the block and print the response
block = notion.delete_block(block)
print(block)
