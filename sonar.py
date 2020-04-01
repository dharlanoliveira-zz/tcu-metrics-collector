import requests
import json


def get_sonar_metrics_on_date(project, metrics, reference_date):
    url = f"http://sonar.cpic.tcu.gov.br/api/measures/search_history?component={project}&from={reference_date}" \
          f"&to={reference_date}&metrics={metrics}"
    r = requests.get(url)
    metrics = {}
    if r.status_code == 200:
        response = json.loads(r.content)
        measures = response['measures']
        for measure in measures:
            metric = measure['metric']
            history = measure['history'][0]
            if 'value' in history:
                value = history['value']
                metrics[metric] = value
            else:
                print(f"Métrica {metric} sem valor")

    return {'endpoint': url, 'metrics': metrics}
