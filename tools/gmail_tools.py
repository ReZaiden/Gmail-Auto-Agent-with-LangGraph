from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)

from utils.config import Config

async def get_gmail_tools():
    """
    A function for return gmail tools:
    - SendMessage
    - CreateDraft
    - Search
    - GetMessage
    - GetThread
    """
    # Get access to gmail
    credentials = get_gmail_credentials(
        token_file=Config.get()['gmail']['token_file'],
        scopes=["https://mail.google.com/"],
        client_sercret_file=Config.get()['gmail']['credentials_file'],

    )

    api_resource = build_resource_service(credentials=credentials)
    toolkit = GmailToolkit(api_resource=api_resource)
    return toolkit.get_tools()
