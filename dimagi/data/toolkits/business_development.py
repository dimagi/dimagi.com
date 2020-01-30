from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Business Development Toolkit"
    ),
    tagline=ugettext_lazy(
        "Use the Business Development Toolkit to develop a BD pipeline "
        "for your organization."
    ),
    image="business-development",
    template="data/toolkits/summaries/business_development.html",
    slug="business-development",
    icon="svg/tookits/icons/business_development.html",
    download_url="https://www.dropbox.com/s/n61uasvfxr44uzu/Dimagi%27s%20BD%20Toolkit.zip?dl=1",
    hubspot_form="c5cf9f9e-75fc-4e1f-942e-8f3e4e9056a7",
)

TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
Building a business development team
at a social enterprise? Use this guide to
jump start your planning.
        """),
        highlight_image="business-development-highlights-one",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
Learn how to project your revenue
and opportunities with the help of
this guide.
        """),
        highlight_image="business-development-highlights-two",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
Understand how your win-rate, total 
expected value, and other key factors impact estimations.
        """),
        highlight_image="business-development-highlights-three",
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.MATURITY_MODEL,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
])
