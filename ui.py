import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

st.title("Triador — Triagem de Chamados de TI")

chamado = st.text_area("Descreva o problema:", height=150)

if st.button("Analisar") and chamado.strip():
    with st.spinner("Analisando..."):
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=PROMPT_SISTEMA + "\n\nChamado: " + chamado
        )
        resultado = json.loads(response.text)

    st.subheader("Resultado")
    st.write(f"**Categoria:** {resultado['categoria']}")
    st.write(f"**Prioridade:** {resultado['prioridade']}")
    st.write(f"**Resposta sugerida:** {resultado['resposta']}")