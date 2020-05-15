from __future__ import absolute_import
from collections import namedtuple


class SummaryGroup(object):

    def __init__(self, title=None, slug=None, description=None):
        self.title = title
        self.slug = slug
        self.description = description
        self.features = []

    def add_summary(self, features):
        self.features.extend(features)


class Summary(object):

    def __init__(self, title=None, description=None, specifics=None, support=None, intensity=None, time=None, security=None):
        self.title = title
        self.description = description
        self.specifics = specifics
        self.intensity = intensity
        self.time = time
        self.security = security
        self.support = support
