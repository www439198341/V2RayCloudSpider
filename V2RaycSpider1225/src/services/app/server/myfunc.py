from urllib.parse import quote

import requests
from sanic.response import json

from services.app.server.apis import apis_admin_get_subs


def get_clash_config(_raw_config):
    url_encoded = quote(_raw_config)
    convert_url = 'http://104.128.91.5:25500/sub?target=clash&url='
    raw_clash_config = requests.get(f'{convert_url}{url_encoded}')
    return raw_clash_config.text.replace('/footers', '/path/323127100515')


def get_clash(token):
    print(token)
    clash_info = apis_admin_get_subs()
    if clash_info.get('msg') != 'success':
        return json(clash_info)
    else:
        return clash_info.get('subscribe')


def get_config(token):
    _config = get_clash(token)
    return requests.get(_config).text if token == 'v2ray' else get_clash_config(_config)
