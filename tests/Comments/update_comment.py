"""Example: Update an existing comment on a Notion page.

This script demonstrates how to modify the content of a comment,
including text and links.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
comment_id = os.getenv("COMMENT_ID")

# Define the updated comment data
data = {
    "rich_text": [
        {
            "text": {
                "content": "Check here",
                "link": {
                    "type": "url",
                    "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                }
            }
        }
    ]
}

# Update the comment and print the response
comments = notion.update_comments(comment_id, data)
print(comments)
