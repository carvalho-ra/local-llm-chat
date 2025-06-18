import streamlit as st
import requests

st.title("Chat com IA Local (Ollama)")

user_msg = st.chat_input("Escreva sua mensagem")

if "msg_list" not in st.session_state:
    st.session_state["msg_list"] = []

for msg in st.session_state["msg_list"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_msg:
    st.chat_message("user").write(user_msg)

    st.session_state["msg_list"].append({
        "role": "user",
        "content": user_msg
    })

    linhas = []
    for m in st.session_state["msg_list"]:
        role = m["role"]
        content = m["content"]
        linha_formatada = f"{role}: {content}"
        linhas.append(linha_formatada)

    prompt = "\n".join(linhas)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    content = response.json()["response"]

    st.chat_message("assistant").write(content)

    st.session_state["msg_list"].append({
        "role": "assistant",
        "content": content
    })
