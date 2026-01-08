"""Class pyNotion for Notion API"""
import requests
import json

class pyNotion:
    """
    Represent Notion connection class.

    Attributes:
        token (str): Notion token.
    """


    def __init__(self, token: str, timeout: int = 10)  -> None:
        """
        Initialize a new pyNotion instance.

        Args:
            token (str): Notion token.
            timeout (int): Request timeout in seconds. Default is 10.
        """

        self.headers = {
            'Authorization': f"Bearer {token}", 
            'Content-Type': 'application/json', 
            'Notion-Version': '2022-06-28'
        }
        self.timeout = timeout

    
    def _print_version(self) -> None:
        print(f"Notion API Version: 0.0.2")

    
    
    def get_pages(self, search_params={"filter": {"value": "page", "property": "object"}}) -> list:
        """
        Get all Notion Pages.

        Args:
            search_params (dict): Search parameters to get Notion Pages.

        Returns:
            list: All pages information.
        """
        search_response = requests.post('https://api.notion.com/v1/search', 
        json=search_params, headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def get_page(self, page_id: str) -> dict:
        """
        Get Notion Page by id.

        Args:
            page_id (str): Notion page id.

        Returns:
            dict: Page information.
        """
        search_response = requests.get(f'https://api.notion.com/v1/pages/{page_id}', 
        headers=self.headers, timeout=self.timeout)

        return search_response.json()
    

    def update_page(self, page_id: str, content: dict) -> dict:
        """
        Update a Notion Page by Id.

        Args:
            page_id (str): Notion page id.
            content (dict): New content for notion page.

        Returns:
            dict: Page information.
        """
        payload = json.dumps(content)
        search_response = requests.patch(f'https://api.notion.com/v1/pages/{page_id}', 
        headers=self.headers, data=payload, timeout=self.timeout)

        return search_response.json()
    

    def archive_page(self, page_id: str) -> dict:
        """
        Archive a Notion Page by Id.

        Args:
            page_id (str): Notion page id.

        Returns:
            dict: Page information.
        """
        payload = json.dumps({
            "archived": True
        })
        search_response = requests.patch(f'https://api.notion.com/v1/pages/{page_id}', 
        headers=self.headers, data=payload, timeout=self.timeout)

        return search_response.json()


    def get_users(self) -> dict:
        """
        Get users information in the notion connector.

        Returns:
            dict: Users information.
        """
        search_response = requests.get(
            'https://api.notion.com/v1/users/', 
            headers=self.headers, timeout=self.timeout)
        
        return search_response.json()

    def create_page_in_page(self, page_id: str, properties: dict) -> dict:
        """
        Create a Notion Page inside Notion Page.

        Args:
            page_id (str): Notion page id.
            properties (dict): Properties of new notion page.

        Returns:
            dict: Pages information.
        """
        payload = json.dumps({
            "parent": {
                "page_id": page_id
            },
            "properties": properties
        })
        search_response = requests.post(
            'https://api.notion.com/v1/pages', 
            headers=self.headers, data=payload, timeout=self.timeout)
        
        return search_response.json()
    

    def create_page_in_database(self, database_id: str, properties: dict) -> dict:
        """
        Create a Notion Page inside Notion Database.

        Args:
            database_id (str): Notion database id.
            properties (dict): Properties of new notion page.

        Returns:
            dict: Page information.
        """
        payload = json.dumps({
            "parent": {
                "database_id": database_id
            },
            "properties": properties
        })
        search_response = requests.post(
            'https://api.notion.com/v1/pages', 
            headers=self.headers, data=payload, timeout=self.timeout)
        
        return search_response.json()


    def get_block(self, page_id: str) -> dict:
        """
        Get block information of notion page.

        Args:
            page_id (str): Notion page id.

        Returns:
            dict: Block information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/blocks/{page_id}', 
            headers=self.headers, timeout=self.timeout)
        
        return search_response.json()


    def get_block_children(self, page_id: str) -> dict:
        """
        Get block children information of notion page.

        Args:
            page_id (str): Notion page id.

        Returns:
            dict: Blocks information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100', 
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def delete_block(self, block_id: str) -> dict:
        """
        Delete a block of notion page.

        Args:
            block_id (str): Notion page id.

        Returns:
            dict: Block information.
        """
        search_response = requests.delete(
            f'https://api.notion.com/v1/blocks/{block_id}', 
            headers=self.headers, timeout=self.timeout)

        return search_response.json()
    

    def update_block(self, block_id: str, content: dict) -> dict:
        """
        Delete a block of notion page.

        Args:
            block_id (str): Notion block id.
            content (dict): New block information.

        Returns:
            dict: Block information.
        """
        payload = json.dumps(content)
        search_response = requests.patch(
            f'https://api.notion.com/v1/blocks/{block_id}', 
            headers=self.headers, data=payload, timeout=self.timeout)
        
        return search_response.json()


    def append_block_children(self, block_id: str, content: dict) -> dict:
        """
        Append a block children in a block of notion page.

        Args:
            block_id (str): Notion page id.
            content (dict): Block children information.

        Returns:
            dict: Block information.
        """
        payload = json.dumps(content)
        search_response = requests.patch(
            f'https://api.notion.com/v1/blocks/{block_id}/children', 
            headers=self.headers, data=payload, timeout=self.timeout)

        return search_response.json()
    

    def get_database(self, database_id: str) -> dict:
        """
        Get notion database information.

        Args:
            database_id (str): Notion database id.

        Returns:
            dict: Database information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/databases/{database_id}', 
            headers=self.headers, timeout=self.timeout)
        
        return search_response.json()
    

    def query_database(self, database_id: str, query: dict) -> dict:
        """
        Search by query in a notion database.

        Args:
            database_id (str): Notion database id.
            query (dict): Query for notion database.

        Returns:
            dict: Database information.
        """
        data = json.dumps(query)
        search_response = requests.post(
            f'https://api.notion.com/v1/databases/{database_id}/query', 
            headers=self.headers, data=data, timeout=self.timeout)
        
        return search_response.json()
    

    def create_database(self, data: dict) -> dict:
        """
        Create a notion database.

        Args:
            data (dict): Notion database information.

        Returns:
            dict: Database information.
        """
        data = json.dumps(data)
        search_response = requests.post(
            f'https://api.notion.com/v1/databases', 
            headers=self.headers, data=data, timeout=self.timeout)
        
        return search_response.json()
    

    def update_database(self, database_id: str, data: dict) -> dict:
        """
        Update a notion database.

        Args:
            database_id (str): Notion database id.
            data (dict): New notion database information.

        Returns:
            dict: Database information.
        """
        data = json.dumps(data)
        search_response = requests.patch(
            f'https://api.notion.com/v1/databases/{database_id}', 
            headers=self.headers, data=data, timeout=self.timeout)

        return search_response.json()
    

    def get_comments(self, block_id: str) -> dict:
        """
        Get all comments in a notion block.

        Args:
            block_id (str): Notion block id.

        Returns:
            dict: Comments information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/comments?block_id={block_id}&page_size=100', 
            headers=self.headers, timeout=self.timeout)
        
        return search_response.json()
    

    def add_comments_discussion(self, data: dict) -> dict:
        """
        Add comments or discussion in a notion block.

        Args:
            data (str): Comment information.

        Returns:
            dict: Pages information.
        """
        data = json.dumps(data)
        search_response = requests.post(
            f'https://api.notion.com/v1/comments', 
            headers=self.headers, data=data)
        
        return search_response.json()