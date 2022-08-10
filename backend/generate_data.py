import requests
import json
from pathlib import Path


def download_data():
    url = 'https://mtgjson.com/api/v5/AtomicCards.json'
    response = requests.get(url)
    with open("data/AtomicCards.json", "w", encoding="utf8") as f:
        f.write(response.text)
        f.close()

def isSimic(card): return card["colorIdentity"] in (["G"], ["U"], ["G", "U"], [])

def isCreature(card): return "Creature" in card["types"]

def isLegal(card): return "commander" in card["legalities"]


def extract_data():
    data_file = Path('data/AtomicCards.json')
    if not data_file.exists():
        download_data()

    cardsFetched = []

    with open('data/AtomicCards.json', 'r', encoding="utf8") as f:
        atomic_cards = json.loads(f.read())

    for cards_with_name in atomic_cards["data"].values():
        cardsFetched.extend(card for card in cards_with_name if isSimic(card) and isCreature(card) and isLegal(card))

    with open('data/cards.json', 'w') as outfile:
        json.dump(cardsFetched, outfile)

    print(f'Cards fetched: {len(cardsFetched)}')

extract_data()