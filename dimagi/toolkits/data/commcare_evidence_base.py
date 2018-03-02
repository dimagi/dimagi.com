from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.toolkits.models import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The CommCare Evidence Base"
    ),
    tagline=ugettext_lazy(
        "Over 50 studies have assessed CommCare's impact, making it the most "
        "evidence-based mobile platform for frontline workers in low-resource "
        "settings."
    ),
    template="toolkits/summaries/commcare_evidence_base.html",
    slug="commcare-evidence-base",
    download_url="https://www.dropbox.com/s/chn7t7dsubhe9qb/CommCare-Evidence-Base-July-2016.pdf?dl=1",
    hubspot_form="f9b416b1-eb8b-430b-a2b6-644481b64a69",
)
