# Triador

Assistente de triagem de chamados de suporte de TI com LLM.

O usuário descreve um problema e o sistema classifica automaticamente a categoria, define a prioridade e sugere uma resposta — tudo via Gemini API.

## Como funciona

1. O chamado é enviado para o modelo Gemini junto com uma base de soluções conhecidas
2. O modelo retorna um JSON estruturado com `categoria`, `prioridade` e `resposta`
3. A interface exibe o resultado em tempo real

## Tecnologias

- Python 3
- Google Gemini API (`google-genai`)
- Streamlit
- python-dotenv

## Como rodar localmente

```bash
git clone https://github.com/lipefp/triador.git
cd triador

python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

cp .env.example .env
# Edite o .env e adicione sua GEMINI_API_KEY

streamlit run ui.py
```

## Estrutura

```
triador/
├── app.py                  # Script de teste via terminal
├── ui.py                   # Interface Streamlit
├── data/
│   └── base_solucoes.json  # Base de soluções conhecidas
├── .env.example
└── requirements.txt
```

## Motivação

Estudo prático de aplicações com LLM aplicado a um problema real: a triagem de chamados de suporte de TI, área em que atuo no dia a dia.