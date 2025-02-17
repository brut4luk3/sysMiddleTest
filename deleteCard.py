import requests
from utils import TRELLO_API_BASE, TRELLO_API_KEY, TRELLO_TOKEN, get_trello_lists, get_trello_cards

def delete_card():
    list_id = get_trello_lists()
    card_id = get_trello_cards(list_id)

    url = f"{TRELLO_API_BASE}/cards/{card_id}"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }

    response = requests.delete(url, params=params)
    
    if response.status_code == 200:
        print(f"Card deletado com sucesso!")
    else:
        print(f"Erro ao deletar card: {response.text}")

if __name__ == "__main__":
    delete_card()