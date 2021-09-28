from __future__ import absolute_import
from collections import namedtuple


class Toolkit(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for toolkit information to avoid errors and merge
    issues.
    """

    def __init__(self, title=None, tagline=None, template=None, slug=None,
                 download_url=None, icon=None, hubspot_form=None,
                 hubspot_formId=None, image=None, download_title=None,
                 french_download_url=None, french_hubspot_form=None,
                 primary_cta=None, subnav_cta=None, event_tracking_title=None,
                 download_slides=None, download_slides_cta=None, language=None):
        self.other_toolkits = []
        self.highlights = []
        self.title = title
        self.download_title = download_title
        self.tagline = tagline
        self.image = image
        self.template = template
        self.slug = slug
        self.download_url = download_url
        self.icon = icon
        self.hubspot_form = hubspot_form
        self.hubspot_formId = hubspot_formId
        self.french_download_url = french_download_url
        self.french_hubspot_form = french_hubspot_form
        self.primary_cta = primary_cta
        self.subnav_cta = subnav_cta
        self.event_tracking_title = event_tracking_title
        self.download_slides = download_slides
        self.download_slides_cta = download_slides_cta
        self.language = language

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

    def __init__(self, name=None, description=None, highlight_image=None):
        self.name = name
        self.description = description
        self.highlight_image = highlight_image


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
        

