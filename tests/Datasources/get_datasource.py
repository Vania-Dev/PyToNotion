"""Example: Retrieve information about a Notion datasource.

This script demonstrates how to fetch details about a specific datasource
using its datasource ID.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))
datasource_id = os.getenv("DATASOURCE_ID")

# Get the datasource information and print it
datasource = notion.get_datasource(datasource_id)
print(datasource)
