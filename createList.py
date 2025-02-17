import requests
from utils import TRELLO_API_BASE, TRELLO_API_KEY, TRELLO_TOKEN, TRELLO_BOARD_ID

def get_highest_pos():
    """Obtém todas as listas do board e retorna o maior valor de `pos`."""
    url = f"{TRELLO_API_BASE}/boards/{TRELLO_BOARD_ID}/lists"
    params = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        lists = response.json()
        if lists:
            max_pos = max([lst["pos"] for lst in lists])  # Encontra o maior `pos`
            return max_pos + 4000  # Mantém a proporção de espaçamento
        else:
            return 1000  # Caso não haja listas, cria com `pos=1000`
    else:
        print("Erro ao buscar listas:", response.text)
        return None

def create_list():
    """Cria uma nova lista no Trello, garantindo que fique sempre à direita."""
    name = input("Digite o nome da nova lista: ")
    new_pos = get_highest_pos()

    if new_pos is None:
        return

    url = f"{TRELLO_API_BASE}/lists"
    params = {
        "name": name,
        "idBoard": TRELLO_BOARD_ID,
        "pos": new_pos,
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }

    response = requests.post(url, params=params)
    
    if response.status_code == 200:
        print(f"Lista '{name}' criada com sucesso na posição {new_pos}!")
    else:
        print(f"Erro ao criar lista: {response.text}")

if __name__ == "__main__":
    create_list()