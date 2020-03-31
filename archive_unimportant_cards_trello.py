from env_vars import env_vars
from trello import get_cards_with_labels, archive_cards_with_id

if __name__ == "__main__":
    all_vars = env_vars()

    trello_key = all_vars['trello.api_key']
    trello_token = all_vars['trello.token']
    board_id = all_vars['trello.board_id']
    cards_to_archive = get_cards_with_labels(board_id, all_vars['trello.production_list'],
                                             all_vars['trello.archived_labels'], trello_key, trello_token)
    archive_cards_with_id(cards_to_archive, trello_key, trello_token)
