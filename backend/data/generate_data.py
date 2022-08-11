import requests
import json
from pathlib import Path


def download_data(bulk_data_file):
    url = 'https://mtgjson.com/api/v5/AtomicCards.json'
    response = requests.get(url)
    with open(bulk_data_file, "w", encoding="utf8") as f:
        f.write(response.text)
        f.close()

def isSimic(card): return card["colorIdentity"] in (["G"], ["U"], ["G", "U"], [])

def isCreature(card): return "Creature" in card["types"]

def isLegal(card): return "commander" in card["legalities"]


def extract_data():
    bulk_data_file = Path('backend/data/json/bulk_data.json')
    filtered_data_file = Path('backend/data/json/cards.json')

    if not bulk_data_file.exists():
        download_data(bulk_data_file)

    cardsFetched = []
    attributes_to_keep = ['name', 'supertypes', 'types', 'subtypes', 'colors', 'colorIdentity' ]
    with open(bulk_data_file, 'r', encoding="utf8") as f:
        bulk_data = json.loads(f.read())

    for cards_with_name in bulk_data["data"].values():
        cardsFetched.extend(card for card in cards_with_name if isSimic(card) and isCreature(card) and isLegal(card))


    for card in cardsFetched:
        for attribute in card.copy():
            if(attribute not in attributes_to_keep):
                del card[attribute]

        
    with open(filtered_data_file, 'w') as outfile:
        json.dump(cardsFetched, outfile)
        outfile.close()
    print(f'Cards fetched: {len(cardsFetched)}')

extract_data()