import requests
from utils import (
    TRELLO_API_BASE, ASANA_API_BASE, 
    TRELLO_API_KEY, TRELLO_TOKEN, TRELLO_BOARD_ID, 
    ASANA_HEADERS, ASANA_WORKSPACE_ID
)

""" Aqui estarei obtendo as listas do Trello no board específico """
def get_trello_lists():
    url = f"{TRELLO_API_BASE}/boards/{TRELLO_BOARD_ID}/lists"
    params = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else []

""" Aqui estarei obtendo os cards de uma lista específica """
def get_trello_cards(list_id):
    url = f"{TRELLO_API_BASE}/lists/{list_id}/cards"
    params = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else []

""" Aqui estarei criando um projeto no Asana com um nome digitado pelo usuário """
def create_asana_project(name):
    url = f"{ASANA_API_BASE}/projects"
    data = {"data": {"name": name, "workspace": ASANA_WORKSPACE_ID}}
    response = requests.post(url, json=data, headers=ASANA_HEADERS)
    
    if response.status_code == 201:
        return response.json()["data"]["gid"]
    else:
        print(f"Erro ao criar projeto no Asana: {response.text}")
        return None

""" Criando uma sessão no projeto criado anteriormente no Asana """
def create_asana_section(name, project_id):
    url = f"{ASANA_API_BASE}/sections"
    data = {"data": {"name": name, "project": project_id}}
    response = requests.post(url, json=data, headers=ASANA_HEADERS)
    
    if response.status_code == 201:
        return response.json()["data"]["gid"]
    else:
        print(f"Erro ao criar seção '{name}': {response.text}")
        return None

""" Criando uma tarefa na sessão criada anteriormente no Asana """
def create_asana_task(name, notes, project_id, section_id):
    url = f"{ASANA_API_BASE}/tasks"
    data = {
        "data": {
            "name": name,
            "notes": notes,
            "projects": [project_id],
            "memberships": [{"project": project_id, "section": section_id}]
        }
    }
    response = requests.post(url, json=data, headers=ASANA_HEADERS)
    
    if response.status_code == 201:
        print(f"Tarefa '{name}' criada no Asana")
    else:
        print(f"Erro ao criar tarefa '{name}': {response.text}")

""" Sincronizando TRELLO > ASANA """
def sync_trello_to_asana():
    
    project_name = input("\nDigite o nome do projeto no Asana: ")
    
    project_id = create_asana_project(project_name) # Criando o projeto
    if not project_id:
        return

    lists = get_trello_lists()
    # Convertendo as listas em sessões
    for trello_list in lists:
        section_id = create_asana_section(trello_list["name"], project_id)
        if not section_id:
            continue

        cards = get_trello_cards(trello_list["id"])
        # Convertendo os cards em tarefas
        for card in cards:
            create_asana_task(card["name"], card["desc"], project_id, section_id)

if __name__ == "__main__":
    sync_trello_to_asana()