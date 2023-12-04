# Import prerequisite libraries
import os
from openai import AzureOpenAI

MODEL = "jun-openai-gpt4" # deployment name

client = AzureOpenAI(
    api_version="2023-12-01-preview",  
    api_key=os.environ["OPENAI_API_KEY"],  
    azure_endpoint=os.environ["OPENAI_API_ENDPOINT"],
)

# chatbot
conversation = [
    {
        "role": "system",
        "content": """
        You are a conversational AI assistant named Cramer that can help people with generating sql query language.
        
        Database schema:
        Table: users
        Columns: id, name, email, phone, address, city, country, zipcode, created_at, updated_at
        """
    },
    {
        "role": "user",
        "content": """
        Human: Where does John live?
        Cramer: SELECT address FROM users WHERE name = 'John'; 
        """
    }
]

while True:
    conversation.append({
        "role": "user",
        "content": input("Human: ")
    })
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
    )
    
    conversation.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })
    print("Cramer: " + response.choices[0].message.content)
