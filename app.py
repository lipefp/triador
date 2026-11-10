import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chamado = "Meu computador não liga depois da atualização do Windows."

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=chamado
)

print(response.text)