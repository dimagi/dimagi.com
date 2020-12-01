from __future__ import absolute_import


class CaseStudy(object):
    """
    Using a class instead of named tuple to handle object changes over time
    as requirements change for project information to avoid errors and merge
    issues.
    """

    def __init__(self, title=None, summary=None, partners=None, countries=None,
                 sectors=None, features=None, slug=None, download_url=None, hubspot_form=None,
                 download_url_language=None, hubspot_form_language=None,
                 primary_cta=None, subnav_cta=None, event_tracking_title=None):
        self.title = title
        self.summary = summary
        self.partners = partners
        self.countries = countries
        self.sectors = sectors
        self.features = features
        self.slug = slug
        self.download_url = download_url
        self.hubspot_form = hubspot_form
        self.download_url_language = download_url_language
        self.hubspot_form_language = hubspot_form_language
        self.primary_cta = primary_cta
        self.subnav_cta = subnav_cta
        self.event_tracking_title = event_tracking_title
