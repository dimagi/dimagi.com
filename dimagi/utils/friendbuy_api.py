from __future__ import absolute_import
import requests
from requests.auth import HTTPBasicAuth

from dimagi.utils.config import setting

ACCESS = setting('FRIENDBUY_ACCESS', '')
SECRET = setting('FRIENDBUY_SECRET', '')
BASE_URL = 'https://api.friendbuy.com/v1'


def _get_url_share(share_id):
    return "{}/shares/{}".format(BASE_URL, share_id)


def get_share(share_id):
    data = requests.get(_get_url_share(share_id),
                        auth=HTTPBasicAuth(ACCESS, SECRET))
    return data.json()
