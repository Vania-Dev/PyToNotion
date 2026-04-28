"""Example: Update an existing block in a Notion page.

This script demonstrates how to modify the content of a specific block,
such as changing a heading's text.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")
block = os.getenv("BLOCK_ID")

# Define the updated content for the block
content = {
            "heading_1": {
                "rich_text": [{
                    "type": "text",
                    "text": { "content": "This is a test of the Notion API"}
                }]
            }
        }

# Update the block and print the response
block = notion.update_block(block, content)
print(block)
