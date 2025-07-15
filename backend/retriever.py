from backend/vector_store import search_vector_store
import os
from dotenv import load_dotenv
from groq import Groq
import openai
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client=Groq(api_key)
def callllm(prompt):
     response=client.chat.completions.create(
         model="mixtral-8x7b-32768",
         messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
         temperature=0.3
     )
     return response.choices[0].message.content
     
