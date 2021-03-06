from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "CommCare + DHIS2 Digital Health Systems"
    ),
    tagline=ugettext_lazy(
        "Learn how CommCare and DHIS2 integrate to create "
        "sustainable data pipelines."
    ),
    image="digital-health-systems",
    template="data/toolkits/summaries/digital_health_systems.html",
    slug="digital-health-systems",
    icon="svg/tookits/icons/dhis.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Toolkits/CommCare%20Integration%20with%20DHIS2.pdf",
    hubspot_form="81378619-a5d7-4d90-b4b0-bb49dfeb3dc9",
    french_download_url="https://cdn2.hubspot.net/hubfs/503070/Toolkits/Inte%CC%81gration%20de%20CommCare%20et%20DHIS2.pdf",
    french_hubspot_form="23a4f46d-db9d-433d-a341-c2ec8e1cacaf",
)

TOOLKIT.add_highlights([
    Highlight(
        description=ugettext_lazy("""
Understand how CommCare and DHIS2 work together to create
an end-to-end data pipeline for your digital health system.
        """),
        highlight_image="digital-health-systems-highlights-one",
    ),
    Highlight(
        description=ugettext_lazy("""
Compare hard and soft costs associated with the DHIS2 and CommCare platforms.
        """),
        highlight_image="digital-health-systems-highlights-two",
    ),
    Highlight(
        description=ugettext_lazy("""
Evaluate the key differences between CommCare and DHIS2 mobile applications.
        """),
        highlight_image="digital-health-systems-highlights-three",
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
    summary.BUSINESS_DEVELOPMENT,
])
