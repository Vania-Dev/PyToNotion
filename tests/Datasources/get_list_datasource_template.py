"""Example: Retrieve available templates for a datasource.

This script demonstrates how to fetch all templates associated with
a specific datasource.
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

# Get the datasource templates and print them
datasource = notion.get_datasource_template(datasource_id)
print(datasource)
