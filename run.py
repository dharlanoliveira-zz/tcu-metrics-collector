import sys
import getopt

from print_cards_funcionalities_trello import print_cards_funcionalities
from print_loc_by_developer import print_loc_by_developer
from print_sonar_metrics import print_sonar_metrics

input_description = "run.py --init_date --end_date"


def extract_range_date():
    global init_date, end_date
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ie:", ["init_date=", "end_date="])
    except getopt.GetoptError:
        print(input_description)
        sys.exit(2)

    if not opts:
        print(input_description)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i", "--init_date"):
            init_date = arg
        elif opt in ("-e", "--end_date"):
            end_date = arg
        else:
            print(input_description)
            sys.exit(2)

    return init_date, end_date


if __name__ == "__main__":
    init_date, end_date = extract_range_date()
    print()
    print()
    print_cards_funcionalities()
    print()
    print()
    print_loc_by_developer(init_date, end_date)
    print()
    print()
    print_sonar_metrics(end_date)
    print()
    print()
