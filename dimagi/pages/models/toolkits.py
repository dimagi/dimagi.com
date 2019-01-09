from __future__ import absolute_import
from collections import namedtuple


class Toolkit(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for toolkit information to avoid errors and merge
    issues.
    """

    def __init__(self, title=None,tagline=None, template=None, slug=None, download_url=None, icon=None, hubspot_form=None, hubspot_formId=None,image=None,):
        self.other_toolkits = []
        self.highlights = []
        self.title = title
        self.tagline = tagline
        self.image = image
        self.template = template
        self.slug = slug
        self.download_url = download_url
        self.icon = icon
        self.hubspot_form = hubspot_form
        self.hubspot_formId = hubspot_formId

    def add_other_toolkits(self, other_toolkits):
        self.other_toolkits.extend(other_toolkits)

    def add_highlights(self, highlights):
        self.highlights.extend(highlights)


class Highlight(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for highlights information to avoid errors and merge
    issues.
    """

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description


class OtherToolkit(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for other toolkits information to avoid errors and merge
    issues.
    """

    def __init__(self, icon=None, name=None, description=None, view_url=None):
        self.icon = icon
        self.name = name
        self.description = description
        self.view_url = view_url
        

