from __future__ import absolute_import


class Employee(object):

    def __init__(self, data):
        self.slug = data['slug']
        self.name = data['name']
        self.image = data['image']
        self.image = self.image
        if self.image:
            self.image = self.image.replace(
                'http://dimagi.wpengine.com', '//dimagi.wpengine.com'
            )
        self.role = data['role']
        self.bio = data['bio']
        self.bio_html = data['bio_html']
        self.short_bio = data['short_bio']
        self.order_exec = data['order_exec'] or 9999
        self.office = data['office_slug']
        self.office_name = data['office_name']


class Office(object):

    def __init__(self, data):
        self.name = data['office']
        self.slug = data['office_slug']
        self.members = [Employee(e) for e in data['members']]
