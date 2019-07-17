from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Digital Health Interventions Checklist"
    ),
    tagline=ugettext_lazy(
        "Learn how to describe your digital health technology across stakeholders "
    ),
    image="digital-health-interventions",
    template="data/toolkits/summaries/digital_health_interventions.html",
    slug="digital-health-interventions",
    icon="svg/tookits/icons/digital_health_interventions.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/ALL_Digital%20Health%20Interventions%20Checklist_v2.pdf",
    hubspot_form="0e1517c2-5a8f-4dca-a442-11252bb305d8",
)

TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
Defines the shared language to describe the 
uses of digital technology for health.
        """),
        highlight_image="digital-health-interventions-highlight-one",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
Shares different sets of recommendations for 
clients, healthcare providers, health system 
managers, and data services.
        """),
        highlight_image="digital-health-interventions-highlight-two",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
Covers recommendations for specific 
initiatives from client health records 
management to health facilities assessment 
and targeted client communications.
        """),
        highlight_image="digital-health-interventions-highlight-three",
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.MATURITY_MODEL,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
])
