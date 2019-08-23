from __future__ import absolute_import
from collections import namedtuple


Support = namedtuple(
    'Support',
    'basic standard advanced custom'
)


class FeatureGroup(object):

    def __init__(self, title=None, slug=None, description=None):
        self.title = title
        self.slug = slug
        self.description = description
        self.features = []

    def add_features(self, features):
        self.features.extend(features)


class Feature(object):

    def __init__(self, title=None, description=None, support=None):
        self.title = title
        self.description = description
        self.support = support
