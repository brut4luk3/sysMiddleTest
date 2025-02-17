import requests
import os
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_BASE = os.getenv("TRELLO_API_BASE")
TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

ASANA_API_BASE = os.getenv("ASANA_API_BASE")
ASANA_ACCESS_TOKEN = os.getenv("ASANA_ACCESS_TOKEN")
ASANA_WORKSPACE_ID = os.getenv("ASANA_WORKSPACE_ID")

ASANA_HEADERS = {
    "Authorization": f"Bearer {ASANA_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def get_trello_lists():
    url = f"{TRELLO_API_BASE}/boards/{TRELLO_BOARD_ID}/lists"
    params = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        lists = response.json()
        for idx, lst in enumerate(lists):
            print(f"{idx + 1}. {lst['name']}")
        choice = int(input("\nEscolha uma lista pelo número: ")) - 1
        return lists[choice]["id"]
    else:
        print("Erro ao buscar listas:", response.text)
        return None

def get_trello_cards(list_id):
    url = f"{TRELLO_API_BASE}/lists/{list_id}/cards"
    params = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        cards = response.json()
        for idx, card in enumerate(cards):
            print(f"{idx + 1}. {card['name']}")
        choice = int(input("\nEscolha um card pelo número: ")) - 1
        return cards[choice]["id"]
    else:
        print("Erro ao buscar cards:", response.text)
        return None