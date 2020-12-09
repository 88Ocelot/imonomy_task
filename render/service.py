import json
import urllib.request
import datetime
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imonomy_task.settings')
django.setup()
from render.models import ApiData

API_KEY = '4e923a83-8b31-4c28-ac3d-f6cb994a60af'
API_URL = 'http://publishers.imonomy.com/api/reports{query_params}'
QUERY_PARAMS = '?key={api_key}&type_name=dsp&format=json&date_from={date_from}&date_to={date_to}'


def _get_api_url(date_from=None, date_to=None):
    if date_from is None or date_to is None:
        date_to = datetime.date.today().strftime('%Y-%m-%d')
        date_from = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    return API_URL.format(query_params=QUERY_PARAMS.format(api_key=API_KEY,
                                                           date_from=date_from,
                                                           date_to=date_to))


def _get_api_response(api_url):
    with urllib.request.urlopen(api_url) as url:
        data = json.loads(url.read().decode())
        print(data)
    return data


if __name__ == '__main__':
    response = _get_api_response(_get_api_url())
    for item in response:
        apidata = ApiData(**item)
        apidata.save()