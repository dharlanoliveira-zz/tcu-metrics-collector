from env_vars import env_vars
from trello import get_cards_description_from_list


def print_cards_funcionalities():
    all_vars = env_vars()

    trello_key = all_vars['trello.api_key']
    trello_token = all_vars['trello.token']
    board_id = all_vars['trello.board_id']

    cards_descriptions = get_cards_description_from_list(board_id, all_vars['trello.function_points_list'], trello_key,
                                                         trello_token)
    print(f"Cartões do trello implementados na lista {all_vars['trello.function_points_list']}")
    print()
    print(*cards_descriptions, sep='\n')
