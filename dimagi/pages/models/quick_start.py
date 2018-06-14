from __future__ import absolute_import
from collections import namedtuple


QuickStartCard = namedtuple(
    'QuickStartCard',
    'icon title description level cta'
)


QuickStartArea = namedtuple(
    'QuickStartArea',
    'slug title sections'
)


QuickStartSection = namedtuple(
    'QuickStartSection',
    'title cards'
)
