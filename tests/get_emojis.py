"""Example: Retrieve all custom emojis from the Notion workspace.

This script demonstrates how to fetch all custom emojis available
in the Notion workspace.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

# Get all custom emojis and print them
emoji = notion.get_emojis()
print(emoji)
