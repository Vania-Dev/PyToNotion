"""Example: Retrieve all users in the Notion workspace.

This script demonstrates how to fetch a list of all users that have
access to the Notion workspace.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

# Get all users and print them
users = notion.get_users()
print(users)
