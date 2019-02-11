from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Mobile Data Collection Research | CommCare Evidence Base"
    ),
    tagline=ugettext_lazy(
        "The CommCare Evidence Base is a collection of mobile data collection research," 
        "with 50+ studies evaluating the impact of mobile data collection in frontline programs."
    ),
    template="data/toolkits/summaries/commcare_evidence_base.html",
    slug="commcare-evidence-base",
    download_url="https://www.dropbox.com/s/chn7t7dsubhe9qb/CommCare-Evidence-Base-July-2016.pdf?dl=1",
    hubspot_form="f9b416b1-eb8b-430b-a2b6-644481b64a69",
)
