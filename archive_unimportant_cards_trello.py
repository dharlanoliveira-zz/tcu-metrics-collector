import requests
import json
from jsonpath_ng import jsonpath, parse


def env_vars():
    variables = {}
    with open("secrets") as variables_file:
        for line in variables_file:
            name, var = line.partition("=")[::2]
            variables[name.strip()] = var.rstrip()
    return variables


def trello_identification_parameters(api_key, token):
    return f"key={api_key}&token={token}"


def jsonpath_item_list(json, json_expression, items):
    jsonpath_expr = parse(json_expression)
    labels = jsonpath_expr.find(json)
    return len(labels)


def get_cards_with_labels(board, list_name, labels):
    trello_id = trello_identification_parameters(all_vars['trello.api_key'], all_vars['trello.token'])
    url = f"https://api.trello.com/1/boards/{board}/lists?cards=open&card_fields=name,labels&{trello_id}"
    r = requests.get(url)
    lists = json.loads(r.content)
    reference_list = next(x for x in lists if x['name'] == list_name)
    cards = reference_list['cards']
    cards_with_label = [c for c in cards
                        if jsonpath_item_list(c, '$..labels[*].name', labels)]
    return [(x['id'], x['name']) for x in cards_with_label if x['id']]


def archive_cards_with_id(cards):
    trello_id = trello_identification_parameters(all_vars['trello.api_key'], all_vars['trello.token'])

    for c_id, name in cards:
        url = f"https://api.trello.com/1/cards/{c_id}?closed=true&{trello_id}"
        r = requests.put(url)
        if r.status_code == 200:
            print(f"Card \"{name}\" arquivado")


if __name__ == "__main__":
    all_vars = env_vars()

    board_id = all_vars['trello.board_id']
    cards_to_archive = get_cards_with_labels(board_id, all_vars['trello.production_list'],
                                             all_vars['trello.archived_labels'])
    archive_cards_with_id(cards_to_archive)
