from PyToNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

page_id = "2dce03e4-e857-803d-b179-f6d318145c37"
page = notion.get_page(page_id)
print(page)