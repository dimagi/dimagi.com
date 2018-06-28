from __future__ import absolute_import
from collections import namedtuple


QuickStartCard = namedtuple(
    'QuickStartCard',
    'icon title description level cta'
)


QuickStartSection = namedtuple(
    'QuickStartSection',
    'title cards'
)


QuickStartArea = namedtuple(
    'QuickStartSection',
    'slug title description sections'
)
