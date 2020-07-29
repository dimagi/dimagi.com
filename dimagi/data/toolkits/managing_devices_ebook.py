from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Managing Devices at Scale"
    ),
    tagline=ugettext_lazy(
        "Key learnings from managing thousands of devices in a "
        "large-scale mobile health project."
    ),
    image="managing-devices-ebook",
    template="data/toolkits/summaries/managing_devices_ebook.html",
    slug="managing-devices-ebook",
    icon="svg/tookits/icons/managingdevices_scale.html",
    download_url="https://www.dropbox.com/s/lk5gujyrk3lm7v7/Managing%20Devices%20at%20Scale.pdf?dl=1",
    hubspot_form="186d64b8-8dcc-45d3-af92-03259efc96a8",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        highlight_image="managing-devices-ebook-highlights-one",
        description=ugettext_lazy("""
Aligning responsibilities across
stakeholders is key while rolling out a
mobile project at scale.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        highlight_image="managing-devices-ebook-highlights-two",
        description=ugettext_lazy("""
Know what details you should
include in your explanation guide
for your device.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        highlight_image="managing-devices-ebook-highlights-three",
        description=ugettext_lazy("""
When should you set up a call center
or help desk for support? Our team
weighs in.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MATURITY_MODEL,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
])
