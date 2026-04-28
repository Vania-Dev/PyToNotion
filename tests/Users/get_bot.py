"""Example: Retrieve information about the bot user.

This script demonstrates how to fetch details about the bot associated
with the current API token.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

# Get the bot information and print it
users = notion.get_bot()
print(users)
