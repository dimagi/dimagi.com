from __future__ import absolute_import

from dimagi.utils.wordpress_api import url_filters


class Employee(object):

    def __init__(self, data):
        self.slug = data['slug']
        self.name = data['name']
        self.image = url_filters(data['image'])
        self.role = data['role']
        self.title_director = data['title_director']
        self.bio = data['bio']
        self.bio_html = data['bio_html']
        self.short_bio = data['short_bio']
        self.order_exec = int(data['order_exec'] or 9999)
        if self.order_exec < 0:
            self.order_exec = 9999
        self.order_management = int(data['order_management'] or 9999)
        if self.order_management < 0:
            self.order_management = 9999
        self.order_executive_committee = int(data['order_executive_committee'] or 9999)
        if self.order_executive_committee < 0:
            self.order_executive_committee = 9999
        self.order_director = int(data['order_director'] or 9999)
        if self.order_director < 0:
            self.order_director = 9999
        self.office = data['office_slug']
        self.office_name = data['office_name']

    @property
    def alt_title(self):
        return self.title_director if self.title_director else self.role


class Office(object):

    def __init__(self, data):
        self.name = data['office']
        self.slug = data['office_slug']
        self.members = sorted(
            [Employee(e) for e in data['members']],
            key=lambda x: (x.order_exec, x.name.split(' ')[-1])
        )
