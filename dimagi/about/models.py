from __future__ import absolute_import


class Employee(object):

    def __init__(self, data):
        self.slug = data['slug']
        self.name = data['name']
        self.image = data['image']
        self.role = data['role']
        self.bio = data['bio']
        self.short_bio = data['short_bio']
        self.order_exec = data['order_exec'] or 9999


class Office(object):

    def __init__(self, data):
        self.name = data['office']
        self.members = [Employee(e) for e in data['members']]
