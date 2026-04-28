"""Example: Retrieve all views from a Notion database.

This script demonstrates how to fetch all views associated with
a specific database.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
db_id = os.getenv("DB_ID")

# Get all views from the database and print them
view = notion.get_all_views(database_id=db_id)
print(view)
