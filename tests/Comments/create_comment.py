"""Example: Create a new comment on a Notion page.

This script demonstrates how to add a comment with a link to a Notion page.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
page_id = os.getenv("PAGE_ID")

# Define the comment data with rich text and link
data = {
    "parent": {"page_id": page_id},
    "rich_text": [
        {
            "text": {
                "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
                "link": {
                    "type": "url",
                    "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                }
            }
        }
    ]
}

# Create the comment and print the response
comments = notion.create_comments(data)
print(comments)
