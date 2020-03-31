import sys
import getopt

from env_vars import env_vars
from sonar import get_sonar_metrics_on_date


def extract_reference_date():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:", ["reference_date="])
    except getopt.GetoptError:
        print('test.py --reference-date')
        sys.exit(2)

    if not opts:
        print('test.py --reference-date')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-r", "--reference_date"):
            data = arg
        else:
            print('test.py --reference-date')
            sys.exit(2)

    return data


if __name__ == "__main__":
    all_vars = env_vars()
    reference_date = extract_reference_date()
    projects = all_vars['sonar.projects'].split(",")
    metrics = all_vars['sonar.key_metrics']
    print(f"Initializing extractor sonar metrics on date {reference_date}")

    for project in projects:
        all_result = get_sonar_metrics_on_date(project, metrics, reference_date)
        metrics_result = all_result['metrics']
        print('-' * 10)
        print(all_result['endpoint'])
        print('-' * 10)
        for m in metrics_result:
            print(m, '=', metrics_result[m])
        print('-' * 10)
