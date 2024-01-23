import streamlit as st
import requests
from requests.exceptions import RequestException

api_url = "http://magno4lves.pythonanywhere.com/tarefas/"

def obter_tarefas():
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        st.error(f"Erro ao obter tarefas: {e}")
        return []

def criar_tarefa(titulo, descricao):
    data = {"titulo": titulo, "tarefa": descricao}
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()
        st.success("Tarefa adicionada com sucesso!")
    except RequestException as e:
        st.error(f"Erro ao criar tarefa: {e}")

def atualizar_tarefa(tarefa_id, titulo, descricao):
    url = f"{api_url}{tarefa_id}"
    data = {"titulo": titulo, "tarefa": descricao}
    try:
        response = requests.put(url, json=data)
        response.raise_for_status()
        st.success("Tarefa atualizada com sucesso!")
    except RequestException as e:
        st.error(f"Erro ao atualizar tarefa: {e}")

def excluir_tarefa(tarefa_id):
    url = f"{api_url}{tarefa_id}"
    try:
        response = requests.delete(url)
        response.raise_for_status()
        st.success("Tarefa excluída com sucesso!")
    except RequestException as e:
        st.error(f"Erro ao excluir tarefa: {e}")

def main():
    st.title("Aplicativo CRUD de Tarefas")

    tarefas = obter_tarefas()

    st.write("### Lista de Tarefas")
    for tarefa in tarefas:
        st.write(f"**ID:** {tarefa['id']}, **Título:** {tarefa['titulo']}, **Tarefa:** {tarefa['tarefa']}")

    st.write("### Adicionar Nova Tarefa")
    novo_titulo = st.text_input("Título da Tarefa:")
    nova_descricao = st.text_area("Descrição da Tarefa:")
    if st.button("Adicionar Tarefa"):
        criar_tarefa(novo_titulo, nova_descricao)

    st.write("### Atualizar Tarefa Existente")
    tarefa_id_atualizar = st.text_input("ID da Tarefa a ser Atualizada:")
    titulo_atualizar = st.text_input("Novo Título da Tarefa:")
    descricao_atualizar = st.text_area("Nova Descrição da Tarefa:")
    if st.button("Atualizar Tarefa"):
        atualizar_tarefa(tarefa_id_atualizar, titulo_atualizar, descricao_atualizar)

    st.write("### Excluir Tarefa")
    tarefa_id_excluir = st.text_input("ID da Tarefa a ser Excluída:")
    if st.button("Excluir Tarefa"):
        excluir_tarefa(tarefa_id_excluir)

if __name__ == "__main__":
    main()
