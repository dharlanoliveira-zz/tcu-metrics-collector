import sys
import getopt

from env_vars import env_vars
from git import get_loc_git_date_range
from collections import Counter

input_description = "xxx"


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
    all_vars = env_vars()
    init_date, end_date = extract_range_date()
    projects = all_vars['git.projects'].split(",")
    developers = all_vars['git.developers']
    print(f"Initializing extractor git loc {init_date} - {end_date} -> projects {projects} -> developers {developers}")

    all_metrics = []
    all_loc = 0
    for project in projects:
        metrics = get_loc_git_date_range(project, developers, init_date, end_date)
        print(f"Projeto: {project}")
        for metric in metrics:
            all_loc += metrics[metric]
            print(f"{metric}: {metrics[metric]}")
        print('-' * 10)

    num_developers = len(developers.split(','))
    print(f"Total LOCs produzidas: {all_loc}")
    print(f"Quantidade de desenvolvedores: {num_developers}")
    print(f"Média LOCs por desenvolvedor: {all_loc / num_developers}")
    print('-' * 10)

