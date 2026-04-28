"""Example: Retrieve all pages from the Notion workspace.

This script demonstrates how to search and retrieve all pages
accessible with the current API token.
"""
from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize PyToNotion client with API key
notion = pyNotion(os.getenv("API_KEY"))

# Retrieve all pages and print the results
pages = notion.get_pages()
print(pages)
