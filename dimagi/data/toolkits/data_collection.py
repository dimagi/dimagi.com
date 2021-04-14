from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Data Collection Guide"
    ),
    tagline=ugettext_lazy(
        "Use this introductory guide to data collection to organize your data collection plan."
    ),
    image="data-collection",
    template="data/toolkits/summaries/data_collection.html",
    slug="data-collection",
    icon="svg/tookits/icons/data_collection.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Pillar%20Page%20PDFs/Guide%20to%20Data%20Collection.pdf",
    hubspot_form="781d61a5-25b1-4cc0-8f58-495a02f26bb1",
)

TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
Learn how to categorize your data requirements, including worker 
and project performance metrics.
        """),
        highlight_image="data-collection-highlight-one",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
Read about the different methods of data collection, including surveys, 
interviews, and observational data collection.
        """),
        highlight_image="data-collection-highlight-two",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
Understand the basics of information workflow diagrams and data 
collection plan outlines.
        """),
        highlight_image="data-collection-highlight-three",
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.MATURITY_MODEL,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
    summary.DIGITAL_WORKFLOW_TEMPLATE,
])
