"""Example: Retrieve information about a Notion database.

This script demonstrates how to fetch details about a specific database
using its database ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
database_id = os.getenv("DB_ID")

# Get the database information and print it
database = notion.get_database(database_id)
print(database)
