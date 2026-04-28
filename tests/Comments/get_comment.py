"""Example: Retrieve a specific comment by its ID.

This script demonstrates how to fetch details about a particular comment
from a Notion page.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
comment_id = os.getenv("COMMENT_ID")

# Get the comment and print it
comments = notion.get_comments(comment_id)
print(comments)
