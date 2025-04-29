# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

#Read the API key from environment
#google_api_key = os.getenv("GOOGLE_API_KEY")

# Create a ChatGoogleGenerativeAI model

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)

# Invoke the model with a message
try:
    result = model.invoke("What is 81 divided by 9?")
    print("Full result:")
    print(result)
    print("Content only:")
    print(result.content)
except Exception as e:
    print(f"Request failed immediately: {e}")

