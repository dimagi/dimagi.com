from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The CommCare Evidence Base"
    ),
    tagline=ugettext_lazy(
        "Over 50 studies have assessed CommCare's impact, making it the most "
        "evidence-based mobile platform for frontline workers in low-resource "
        "settings."
    ),
    image="commcare-evidence-base",
    template="data/toolkits/summaries/commcare_evidence_base.html",
    slug="commcare-evidence-base",
    icon="svg/tookits/icons/commcare_evidence_base.html",
    download_url="https://www.dropbox.com/s/chn7t7dsubhe9qb/CommCare-Evidence-Base-July-2016.pdf?dl=1",
    hubspot_form="f9b416b1-eb8b-430b-a2b6-644481b64a69",
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
took 75% less time...
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
21.5% more visits than control group over
a 12-month period.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.MATURITY_MODEL,
    summary.DIGITAL_HEALTH_INTERVENTIONS,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
])
