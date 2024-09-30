import os 
from dotenv import load_dotenv
load_dotenv()

import nest_asyncio
nest_asyncio.apply()

from llama_parse import LlamaParse

os.environ["LLAMA_CLOUD_API_KEY"] = os.getenv("LLAMA_CLOUD_API_KEY")

def ocr(file):
    text = LlamaParse(
    result_type="text"
    ).load_data(file)
    return text[0].text
