from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Mobile Data Collection Guide"
    ),
    tagline=ugettext_lazy(
        "Learn how to set up a mobile data collection program."
    ),
    image="mobile-data-collection",
    template="data/toolkits/summaries/mobile_data_collection.html",
    slug="mobile-data-collection",
    icon="svg/tookits/icons/mobile_data_collection.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Pillar%20Page%20PDFs/Guide%20to%20Mobile%20Data%20Collection.pdf",
    hubspot_form="a6b961bf-2a93-4d93-b2b5-46f71f82fd72",
)

TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
Learn how your data requirements and the environmental implications of your 
program inform your choice of mobile platform.
        """),
        highlight_image="mobile-data-collection-highlight-one",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
Identify your user stories, design the structure of your system, and develop your 
content and delivery design.
        """),
        highlight_image="mobile-data-collection-highlight-two",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
Discover all the different tests to put your application through – from quality assurance, 
usability testing, and pilot programs.
        """),
        highlight_image="mobile-data-collection-highlight-three",
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.MATURITY_MODEL,
    summary.DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
    summary.DIGITAL_WORKFLOW_TEMPLATE,
])
