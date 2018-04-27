from __future__ import absolute_import

from dimagi.utils.wordpress_api import url_filters


class Employee(object):

    def __init__(self, data):
        self.slug = data['slug']
        self.name = data['name']
        self.image = url_filters(data['image'])
        self.role = data['role']
        self.bio = data['bio']
        self.bio_html = data['bio_html']
        self.short_bio = data['short_bio']
        self.order_exec = int(data['order_exec'] or 9999)
        if self.order_exec < 0:
            self.order_exec = 9999
        self.office = data['office_slug']
        self.office_name = data['office_name']


class Office(object):

    def __init__(self, data):
        self.name = data['office']
        self.slug = data['office_slug']
        self.members = sorted(
            [Employee(e) for e in data['members']],
            key=lambda x: (x.order_exec, x.name.split(' ')[-1])
        )
