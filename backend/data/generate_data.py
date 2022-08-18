import requests
import json
from pathlib import Path

atomic_cards = Path('backend/data/json/AtomicCards.json')
simic_cards = Path('backend/data/json/cards.json')
meta = Path('backend/data/json/Meta.json')
meta_url = 'https://mtgjson.com/api/v5/Meta.json'
atomic_cards_url = 'https://mtgjson.com/api/v5/AtomicCards.json'


def download_data(data_file, url):
    response = requests.get(url)
    with open(data_file, "w", encoding="utf8") as f:
        f.write(response.text)
        f.close()

def isSimic(card): return card["colorIdentity"] in (["G"], ["U"], ["G", "U"], [])

def isCreature(card): return "Creature" in card["types"]

def isLegal(card): return "commander" in card["legalities"]

def extract_data(atomic_cards):
    cardsFetched = []
    attributes_to_keep = ['name', 'supertypes', 'types', 'subtypes', 'manaCost', 'identifiers' ]

    with open(atomic_cards, 'r', encoding="utf8") as f:
        bulk_data = json.loads(f.read())

    for cards_with_name in bulk_data["data"].values():
        cardsFetched.extend(card for card in cards_with_name if isSimic(card) and isCreature(card) and isLegal(card))

    for card in cardsFetched:
        for attribute in card.copy():
            if(attribute not in attributes_to_keep):
                del card[attribute]

    with open(simic_cards, 'w') as outfile:
        json.dump(cardsFetched, outfile)
        outfile.close()
    print(len(cardsFetched))

def check_versions(meta, atomic_cards):
    with open(meta, "r", encoding="utf8") as f:
        meta_data = json.loads(f.read())
        f.close()
    with open(atomic_cards, "r", encoding="utf8") as f:
        atomic_cards = json.loads(f.read())
        f.close()
    if meta_data['meta']['version'] == atomic_cards['meta']['version']:
        return True

def check_data():
    if not meta.exists():
        download_data(meta, meta_url)
    if not atomic_cards.exists():
        download_data(atomic_cards, atomic_cards_url)
    if not simic_cards.exists():
        extract_data(atomic_cards)

def daily_data_download():
    print("Starting daily data download.")
    check_data()
    if not check_versions(meta, atomic_cards):
        download_data(atomic_cards, atomic_cards_url)
        extract_data(atomic_cards)
