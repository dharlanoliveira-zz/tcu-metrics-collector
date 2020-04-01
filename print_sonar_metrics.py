from env_vars import env_vars
from sonar import get_sonar_metrics_on_date


def print_sonar_metrics(reference_date):
    all_vars = env_vars()
    projects = all_vars['sonar.projects'].split(",")
    metrics = all_vars['sonar.key_metrics']
    print(f"Coletando métricas sonar na data {reference_date}")
    print()
    for project in projects:
        all_result = get_sonar_metrics_on_date(project, metrics, reference_date)
        metrics_result = all_result['metrics']
        print()
        print(f"Projeto: {project}")
        print(f"URL: {all_result['endpoint']}")
        print()
        for m in metrics_result:
            print(m, '=', metrics_result[m])
