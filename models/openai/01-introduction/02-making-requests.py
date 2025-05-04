from openai import OpenAI
import os

# The OpenAI class will automatically use the OPENAI_API_KEY environment variable
client =OpenAI(api_key=os.getenv("PRIVATE_OPENAI_API_KEY"))
