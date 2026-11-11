import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Carrega a base de soluções
with open("data/base_solucoes.json", "r", encoding="utf-8") as f:
    base_solucoes = json.load(f)

base_texto = "\n".join(
    f"- {item['categoria']}: {item['problema']} → {item['solucao']}"
    for item in base_solucoes
)

PROMPT_SISTEMA = f"""
Você é um assistente de triagem de chamados de suporte de TI.
Use a base de soluções abaixo como referência ao responder:

{base_texto}

Analise o chamado e responda APENAS com um JSON válido, sem texto extra, neste formato:
{{
  "categoria": "<categoria do problema>",
  "prioridade": "<Baixa | Média | Alta | Crítica>",
  "resposta": "<resposta sugerida para o usuário em português>"
}}

Categorias possíveis: Hardware, Software, Rede, Acesso, Impressora, Outro.
"""

chamado = "Meu computador não liga depois da atualização do Windows."

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=PROMPT_SISTEMA + "\n\nChamado: " + chamado
)

resultado = json.loads(response.text)
print(json.dumps(resultado, indent=2, ensure_ascii=False))