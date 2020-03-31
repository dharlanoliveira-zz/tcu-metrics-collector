import requests
import json
from jsonpath_ng import parse


def jsonpath_item_list(json_item, json_expression, items):
    jsonpath_expr = parse(json_expression)
    labels = jsonpath_expr.find(json_item)
    return len(labels)


def trello_identification_parameters(key, token):
    return f"key={key}&token={token}"


def archive_cards_with_id(cards, key, token):
    trello_id = trello_identification_parameters(key, token)

    for c_id, name in cards:
        url = f"https://api.trello.com/1/cards/{c_id}?closed=true&{trello_id}"
        r = requests.put(url)
        if r.status_code == 200:
            print(f"Card \"{name}\" arquivado")


def get_cards_description_from_list(board, list_name, key, token):
    cards = get_cards_from_list(board, list_name, key, token)
    return [c['name'] for c in cards]


def get_cards_with_labels(board, list_name, labels, key, token):
    cards = get_cards_from_list(board, list_name, key, token)
    cards_with_label = [c for c in cards
                        if jsonpath_item_list(c, '$..labels[*].name', labels)]
    return [(x['id'], x['name']) for x in cards_with_label if x['id']]


def get_cards_from_list(board, list_name, key, token):
    trello_id = trello_identification_parameters(key, token)
    url = f"https://api.trello.com/1/boards/{board}/lists?cards=open&card_fields=name,labels&{trello_id}"
    r = requests.get(url)
    lists = json.loads(r.content)
    reference_list = next(x for x in lists if x['name'] == list_name)
    cards = reference_list['cards']
    return cards
