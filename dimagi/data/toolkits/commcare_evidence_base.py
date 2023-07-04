from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The CommCare Evidence Base Overview"
    ),
    download_title=ugettext_lazy(
        "The CommCare Evidence Base Overview"
    ),
    tagline=ugettext_lazy(
        "More studies have assessed CommCare's impact than any "
        "other mobile platform for frontline workers"
    ),
    image="commcare-evidence-base",
    template="data/toolkits/summaries/commcare_evidence_base.html",
    slug="commcare-evidence-base",
    icon="svg/toolkits/icons/commcare_evidence_base.html",
    theme="primary-theme",
    download_url="https://f.hubspotusercontent20.net/hubfs/503070/Toolkits/CommCare%20Evidence%20Base.pdf",
    hubspot_form="f9b416b1-eb8b-430b-a2b6-644481b64a69",
    french_download_url="https://sites.dimagi.com/hubfs/Toolkits/La%20Base%20de%20Evidencias%20de%20CommCare.pdf",
    french_hubspot_form="ad94e7c0-7b6d-469f-8e2e-b8d8f86e3d75",
    event_tracking_title="Evidence Base - ESP ",
    language="spanish",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        highlight_image="commcare-evidence-base-highlights-one",
        description=ugettext_lazy("""
An RCT in South Africa found that
FLWs using CommCare for
cardiovascular disease (CVD) screenings
took 75% less time.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        highlight_image="commcare-evidence-base-highlights-two",
        description=ugettext_lazy("""
In a study with Pathfinder
international, the use of CommCare
helped increase the provisionof HIV
tests from 67.5% to 82.2%.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        highlight_image="commcare-evidence-base-highlights-three",
        description=ugettext_lazy("""
After incorprating performance feedback,
frontline workers in one study made
24% more visits than control group over
a 12-month period.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
    summary.DIGITAL_WORKFLOW_TEMPLATE,
])
