from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Managing Data in CommCare"
    ),
    tagline=ugettext_lazy(
        "A starter guide to inspecting, cleaning and exporting data in "
        "CommCare."
    ),
    image="commcare-managing-data",
    template="data/toolkits/summaries/commcare_managing_data.html",
    slug="commcare-managing-data",
    icon="svg/tookits/icons/managingdata_commcare.html",
    theme="orange-theme",
    download_url="https://sites.dimagi.com/hubfs/Toolkits/Managing%20Data%20in%20CommCare.pdf",
    hubspot_form="f59879b3-23cb-41a6-b4f8-e1daa8ba4141",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        highlight_image="commcare-evidence-base-highlights-one",
        description=ugettext_lazy("""
Improve data cleanliness for accurate reporting and analysis.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        highlight_image="commcare-evidence-base-highlights-two",
        description=ugettext_lazy("""
Understand best practices for exporting data.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        highlight_image="commcare-evidence-base-highlights-three",
        description=ugettext_lazy("""
Learn how to inspect and clean raw data.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_EVIDENCE_BASE,
    summary.MANAGING_DEVICES_EBOOK,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
    summary.DIGITAL_WORKFLOW_TEMPLATE,
])
