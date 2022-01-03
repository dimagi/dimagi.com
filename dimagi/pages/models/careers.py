from __future__ import absolute_import

import html

from django.utils.translation import ugettext


class JobPost(object):

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = html.unescape(data['content'])
        self.departments = [
            ugettext("{} Team").format(d['name']) for d in data['departments']
        ]
        self.employment_type = "Full-Time"
        for metadata in data['metadata']:
            if metadata.get('name') == 'Employment Type':
                self.employment_type = metadata['value']
        self.primary_location = data.get('location', {}).get('name')
        self.locations = [o['location'] for o in data['offices']]
