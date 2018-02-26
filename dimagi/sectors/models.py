from __future__ import absolute_import
from collections import namedtuple


Area = namedtuple(
    'Area',
    'name theme',
)

Country = namedtuple(
    'Country',
    'name icon',
)

Resource = namedtuple(
    'Resource',
    'url name',
)


class Sector(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for sector information to avoid errors and merge
    issues.
    """

    def __init__(self, name=None, summary=None, template=None, slides=None,
                 slug=None, area=None):
        self.name = name
        self.summary = summary
        self.template = template
        self.slides = slides
        self.slug = slug
        self.area = area
        self.projects = []
        self.case_studies = []
        self.additional_resources = []

    def add_projects(self, projects):
        self.projects.extend(projects)

    def add_case_studies(self, studies):
        self.case_studies.extend(studies)

    def add_resources(self, resources):
        self.additional_resources.extend(resources)


class Project(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for project information to avoid errors and merge
    issues.
    """

    def __init__(self, name=None, country=None, description=None, video_url=None,
                 published_study_url=None, commcare_app_url=None):
        self.name = name
        self.country = country
        self.description = description
        self.video_url = video_url
        self.published_study = published_study_url
        self.commcare_app_url = commcare_app_url
