import json
from pprint import pprint

def get_creatures(input_list):
    creature_list = []
    subtypes = {}
    duplicate_subtypes = {}
    single_subtypes = {}
    try:
        with open('backend/data/json/cards.json', 'r') as f:
            card_list = json.load(f)
        for input in input_list:
            creature_list.extend(card for card in card_list if input == card['name'])
        for creature in creature_list:
            for st in creature["subtypes"]:
                if st not in subtypes:
                    subtypes[st] = []
                subtypes[st].append(creature)
        for key, value in subtypes.items():
            if len(value) > 1:
                duplicate_subtypes[key] = value
            else:
                single_subtypes[key] = value
    except Exception as e:
        return e
    return duplicate_subtypes, single_subtypes