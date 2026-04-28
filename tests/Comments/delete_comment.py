"""Example: Delete a comment from a Notion page.

This script demonstrates how to remove a specific comment using its ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
comment_id = os.getenv("DEL_COMMENT_ID")

# Delete the comment and print the response
comments = notion.delete_comments(comment_id)
print(comments)
