from env_vars import env_vars
from trello import get_cards_description_from_list

if __name__ == "__main__":
    all_vars = env_vars()

    trello_key = all_vars['trello.api_key']
    trello_token = all_vars['trello.token']
    board_id = all_vars['trello.board_id']

    cards_descriptions = get_cards_description_from_list(board_id, all_vars['trello.function_points_list'], trello_key,
                                                         trello_token)

    print(*cards_descriptions, sep='\n')
