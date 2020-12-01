from __future__ import absolute_import
import requests

from dimagi.utils.config import setting

API_KEY = setting('HUBSPOT_API_KEY', '')
BASE_URL = 'https://api.hubapi.com/contacts/v1'


def _get_url_update_contact(email):
    return "{}/contact/createOrUpdate/email/{}?hapikey={}".format(
        BASE_URL, email, API_KEY
    )


def update_contact(email, properties):
    """
    :param email:
    :param properties: a list of tuples (property, value)
    :return:
    """
    properties = [{'property': p[0], 'value': p[1]} for p in properties]
    url = _get_url_update_contact(email)
    return requests.post(url, json={
        'properties': properties,
    })


def activate_hubspot_cta(request, cta_id, tracking_name):
    if not hasattr(request, 'hubspot_ctas'):
        request.hubspot_ctas = {}
    request.hubspot_ctas.update({cta_id: tracking_name})
