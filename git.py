import requests
import re


def get_loc_git_date_range(project, developers, init_date, end_date):
    url = f"http://line-count.producao.rancher.tcu.gov.br/sti/{project}/commits?" \
          f"autores={developers}&datainicio={init_date}&datafim={end_date}"
    r = requests.get(url)
    metrics = {}
    if r.status_code == 200:
        locs = re.findall("([xX][0-9]{11}): ([0-9]*)", str(r.content))
        for user, loc in locs:
            metrics[user] = int(loc)
    return metrics
