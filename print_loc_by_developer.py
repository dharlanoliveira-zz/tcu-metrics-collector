from env_vars import env_vars
from git import get_loc_git_date_range


def print_loc_by_developer(init_date, end_date):
    all_vars = env_vars()
    projects = all_vars['git.projects'].split(",")
    developers = all_vars['git.developers']
    print(f"Contando linhas de código produzidas entre {init_date} - {end_date} -> nos projectos {projects} "
          f"-> pelos desenvolvedores {developers}")
    all_loc = 0
    for project in projects:
        result = get_loc_git_date_range(project, developers, init_date, end_date)
        metrics = result['metrics']
        print()
        print(f"Projeto: {project}")
        print(f"URL: {result['endpoint']}")
        for metric in metrics:
            all_loc += metrics[metric]
            print(f"{metric}: {metrics[metric]}")

    num_developers = len(developers.split(','))
    print()
    print(f"Total LOCs produzidas: {all_loc}")
    print(f"Quantidade de desenvolvedores: {num_developers}")
    print(f"Média LOCs por desenvolvedor: {all_loc / num_developers}")
    print('-' * 10)
