import requests
from utils import TRELLO_API_BASE, TRELLO_API_KEY, TRELLO_TOKEN, get_trello_lists

def create_card():
    list_id = get_trello_lists()
    name = input("Digite o nome do card: ")
    description = input("Digite a descrição do card: ")

    url = f"{TRELLO_API_BASE}/cards"
    params = {
        "name": name,
        "desc": description,
        "idList": list_id,
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }

    response = requests.post(url, params=params)
    
    if response.status_code == 200:
        print(f"Card '{name}' criado com sucesso!")
    else:
        print(f"Erro ao criar card: {response.text}")

if __name__ == "__main__":
    create_card()