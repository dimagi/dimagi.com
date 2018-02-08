from __future__ import absolute_import
from collections import namedtuple


Sector = namedtuple(
    'Sector',
    'name summary template slides slug area projects case_studies'
)

Project = namedtuple(
    'Project',
    'name country description video_url',
)

Area = namedtuple(
    'Area',
    'name theme',
)

Country = namedtuple(
    'Country',
    'name icon',
)
