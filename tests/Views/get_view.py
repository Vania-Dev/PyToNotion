"""Example: Retrieve information about a specific view.

This script demonstrates how to fetch details about a particular view
using its view ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

view_id = os.getenv("VIEW_ID")

# Get the view information and print it
view = notion.get_view(view_id)
print(view)
