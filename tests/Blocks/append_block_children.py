"""Example: Append child blocks to a Notion page or block.

This script demonstrates how to add new content blocks (heading, paragraph)
to an existing Notion page.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Define the content blocks to append
content ={
        "children": [
            {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                {
                    "type": "text",
                    "text": {
                    "content": "Lacinato kale"
                    }
                }
                ]
            }
            },
            {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                {
                    "type": "text",
                    "text": {
                    "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                    "link": {
                        "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                    }
                    }
                }
                ]
            }
            }
        ]
        }

# Append the blocks and print the response
block = notion.append_block_children(page_id, content)
print(block)
