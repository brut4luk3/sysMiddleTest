import requests
from utils import TRELLO_API_BASE, TRELLO_API_KEY, TRELLO_TOKEN, get_trello_lists, get_trello_cards

def update_card():
    list_id = get_trello_lists()
    card_id = get_trello_cards(list_id)
    new_list_id = get_trello_lists()

    url = f"{TRELLO_API_BASE}/cards/{card_id}"
    params = {
        "idList": new_list_id,
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }

    response = requests.put(url, params=params)
    
    if response.status_code == 200:
        print(f"Card movido com sucesso!")
    else:
        print(f"Erro ao mover card: {response.text}")

if __name__ == "__main__":
    update_card()