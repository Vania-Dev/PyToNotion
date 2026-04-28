"""PyToNotion - A Python library for interacting with the Notion API.

This module provides a comprehensive interface to work with Notion's API,
including pages, databases, blocks, comments, users, views, and datasources.

Notion API Documentation: https://developers.notion.com/guides/get-started/overview
Notion API Version: 2026-03-11
"""
import requests
import json

class pyNotion:
    """
    Main class for interacting with the Notion API.

    This class provides methods to manage Notion pages, databases, blocks,
    comments, users, views, datasources, and emojis.

    API Documentation: https://developers.notion.com/guides/get-started/overview
    API Version: 2026-03-11

    Attributes:
        headers (dict): HTTP headers for API requests including authorization.
        timeout (int): Request timeout in seconds.

    Example:
        >>> from PyToNotion.pyNotion import pyNotion
        >>> notion = pyNotion(token="your_notion_token")
        >>> page = notion.get_page("page_id")
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
            'Notion-Version': '2026-03-11'
        }
        self.timeout = timeout


    def _print_version(self) -> None:
        print(f"Notion API Version: 1.0.0")


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


    def get_page_by_property(self, page_id: str, property:str) -> dict:
        """
        Get a specific property from a Notion Page.

        Args:
            page_id (str): Notion page id.
            property (str): Notion page property id or name.

        Returns:
            dict: Property information from the page.
        """
        search_response = requests.get(f'https://api.notion.com/v1/pages/{page_id}/properties/{property}',
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


    def move_page(self, page_id: str, content: dict) -> dict:
        """
        Move a Notion Page by Id into Page or Database .

        Args:
            page_id (str): Notion page id.
            content (dict): Move content for notion page.

        Returns:
            dict: Page information.
        """
        payload = json.dumps(content)
        search_response = requests.post(f'https://api.notion.com/v1/pages/{page_id}/move',
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


    def get_user(self, user_id: str) -> dict:
        """
        Get specific user information by user ID.

        Args:
            user_id (str): Notion user id.

        Returns:
            dict: User information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/users/{user_id}',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def get_bot(self) -> dict:
        """
        Get information about the bot user associated with the API token.

        Returns:
            dict: Bot user information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/users/me',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def create_page(self, page_id: str, properties: dict) -> dict:
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
        Update a block of notion page.

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


    def get_all_comments(self, block_id: str) -> dict:
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


    def get_comments(self, comment_id: str) -> dict:
        """
        Get a specific comment by its ID.

        Args:
            comment_id (str): Notion comment id.

        Returns:
            dict: Comment information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/comments/{comment_id}',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def delete_comments(self, comment_id: str) -> dict:
        """
        Delete a specific comment by its ID.

        Args:
            comment_id (str): Notion comment id.

        Returns:
            dict: Deletion confirmation.
        """
        search_response = requests.delete(
            f'https://api.notion.com/v1/comments/{comment_id}',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def create_comments(self, data: dict) -> dict:
        """
        Create a new comment in a Notion page or block.

        Args:
            data (dict): Comment information including parent and rich_text.

        Returns:
            dict: Created comment information.
        """
        data = json.dumps(data)
        search_response = requests.post(
            f'https://api.notion.com/v1/comments',
            headers=self.headers, data=data, timeout=self.timeout)
        return search_response


    def update_comments(self, comment_id: str, data: dict) -> dict:
        """
        Update an existing comment in a Notion page or block.

        Args:
            comment_id (str): Notion Comment id.
            data (dict): Updated comment information.

        Returns:
            dict: Updated comment information.
        """
        data = json.dumps(data)
        search_response = requests.patch(
            f'https://api.notion.com/v1/comments/{comment_id}',
            headers=self.headers, data=data, timeout=self.timeout)
        return search_response


    def create_datasource(self, data: dict) -> dict:
        """
        Create a new datasource in Notion.

        Args:
            data (dict): Datasource configuration including parent and properties.

        Returns:
            dict: Created datasource information.
        """
        data = json.dumps(data)
        search_response = requests.post(
            f'https://api.notion.com/v1/data_sources',
            headers=self.headers, data=data, timeout=self.timeout)

        return search_response.json()


    def get_datasource(self, data_source_id: str) -> dict:
        """
        Get datasource information by ID.

        Args:
            data_source_id (str): Notion Data source id.

        Returns:
            dict: Datasource information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/data_sources/{data_source_id}',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def get_datasource_template(self, data_source_id: str) -> dict:
        """
        Get available templates for a datasource.

        Args:
            data_source_id (str): Notion Data source id.

        Returns:
            dict: Datasource templates information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/data_sources/{data_source_id}/templates',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def query_datasource(self, data_source_id: str, query: dict = {}) -> dict:
        """
        Search by query in a notion database.

        Args:
            data_source_id (str): Notion Data source id.
            query (dict): Query for notion database.

        Returns:
            dict: Database information.
        """
        data = json.dumps(query)
        search_response = requests.post(
            f'https://api.notion.com/v1/data_sources/{data_source_id}/query',
            headers=self.headers, data=data, timeout=self.timeout)

        return search_response.json()


    def update_datasource(self, data_source_id: str, data: dict) -> dict:
        """
        Update an existing datasource.

        Args:
            data_source_id (str): Notion Data source id.
            data (dict): Updated datasource properties.

        Returns:
            dict: Updated datasource information.
        """
        data = json.dumps(data)
        search_response = requests.patch(
            f'https://api.notion.com/v1/data_sources/{data_source_id}',
            headers=self.headers, data=data, timeout=self.timeout)

        return search_response.json()


    def get_view(self, view_id: str) -> dict:
        """
        Get view information by ID.

        Args:
            view_id (str): Notion view id.

        Returns:
            dict: View information.
        """
        search_response = requests.patch(
            f'https://api.notion.com/v1/views/{view_id}',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def get_all_views(self, database_id: str = None, data_source_id: str = None, page_size: int = 100) -> list:
        """
        List all views from a Notion database.
        Args:
            database_id:    ID of the Notion database.
            data_source_id: ID of the data source (includes linked views across the workspace).
            page_size:      Number of results per page (max. 100).
        Returns:
            list: List with all views found.
        """
        if not database_id and not data_source_id:
            return "At least one of database_id or data_source_id must be provided"

        params = {"page_size": page_size}

        if database_id:
            params["database_id"] = database_id
        if data_source_id:
            params["data_source_id"] = data_source_id

        response = requests.get(
            "https://api.notion.com/v1/views",
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )
        data = response.json()

        return data


    def create_view(self, data: dict) -> dict:
        """
        Create a new view in a Notion database.

        Args:
            data (dict): View configuration including type, name, and properties.

        Returns:
            dict: Created view information.
        """
        data = json.dumps(data)
        search_response = requests.post(
            f'https://api.notion.com/v1/views',
            headers=self.headers, data=data, timeout=self.timeout)

        return search_response.json()


    def update_view(self, view_id: str, data: dict) -> dict:
        """
        Update an existing view in a Notion database.

        Args:
            view_id (str): Notion view id.
            data (dict): Updated view properties.

        Returns:
            dict: Updated view information.
        """
        data = json.dumps(data)
        search_response = requests.patch(
            f'https://api.notion.com/v1/views/{view_id}',
            headers=self.headers, data=data, timeout=self.timeout)

        return search_response.json()


    def delete_view(self, view_id: str) -> dict:
        """
        Delete view in notion database.

        Args:
            view_id (str): Notion view id.

        Returns:
            dict: View information.
        """
        search_response = requests.delete(
            f'https://api.notion.com/v1/views/{view_id}',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()


    def get_emojis(self) -> dict:
        """
        Get all custom emojis available in the Notion workspace.

        Returns:
            dict: List of custom emojis with their information.
        """
        search_response = requests.get(
            f'https://api.notion.com/v1/custom_emojis?page_size=100',
            headers=self.headers, timeout=self.timeout)

        return search_response.json()
