# configuration and environment variables
import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key(): 
    key = os.getenv("GEMINI_API_KEY")
    if not key: 
        # handle error nicely in the cli app, returning none for now
        return None
    return key


# default to nice mode....
GIT_INTERVIEWER_MODE = os.getenv("GIT_INTERVIEWER_MODE", "nice")

