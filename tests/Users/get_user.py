"""Example: Retrieve information about a specific user.

This script demonstrates how to fetch details about a Notion user
using their user ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
user_id = os.getenv("USER_ID")

# Get the user information and print it
users = notion.get_user(user_id)
print(users)
