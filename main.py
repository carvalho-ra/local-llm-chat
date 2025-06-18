# install ollama
# curl -fsSL https://ollama.com/install.sh | sh
# ollama pull llama3
# ollama serve
# http://localhost:11434


import streamlit as st  # Interface do usuário
import requests         # Para fazer requisições HTTP (usado para conversar com a IA local)

# Título do app
st.title("Chat com IA Local (Ollama)")

# Campo para o usuário digitar sua mensagem
user_msg = st.chat_input("Escreva sua mensagem")

# Criar lista de mensagens na sessão, se ainda não existir
# Isso garante que o histórico de conversa persista entre interações
if "msg_list" not in st.session_state:
    st.session_state["msg_list"] = []

# Mostrar todas as mensagens anteriores na tela
for msg in st.session_state["msg_list"]:
    st.chat_message(msg["role"]).write(msg["content"])  # role: 'user' ou 'assistant'

# Quando o usuário envia uma nova mensagem
if user_msg:
    # Exibe a mensagem do usuário no chat
    st.chat_message("user").write(user_msg)

    # Adiciona a nova mensagem ao histórico
    st.session_state["msg_list"].append({
        "role": "user",
        "content": user_msg
    })

    # Construir o prompt com o histórico da conversa
    # (versão mais explícita, com explicações)
    linhas = []
    for m in st.session_state["msg_list"]:
        role = m["role"]       # 'user' ou 'assistant'
        content = m["content"] # texto da mensagem
        linha_formatada = f"{role}: {content}"
        linhas.append(linha_formatada)

    # Junta todas as linhas com quebras de linha
    prompt = "\n".join(linhas)

    # Enviar o prompt para o modelo Ollama local
    response = requests.post(
        "http://localhost:11434/api/generate",  # Rota padrão do Ollama local
        json={
            "model": "llama3",  # Nome do modelo (ex: llama3, mistral, phi)
            "prompt": prompt,   # Todo o contexto da conversa
            "stream": False     # Espera a resposta completa antes de retornar
        }
    )

    # Extrai a resposta da IA do JSON
    content = response.json()["response"]

    # Exibe a resposta da IA na interface
    st.chat_message("assistant").write(content)

    # Armazena a resposta no histórico de mensagens
    st.session_state["msg_list"].append({
        "role": "assistant",
        "content": content
    })
