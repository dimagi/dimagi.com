from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.toolkits.models import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Managing Data in CommCare "
    ),
    tagline=ugettext_lazy(
        "A starter guide to inspecting, cleaning and exporting data in "
        "CommCare"
    ),
    template="toolkits/summaries/commcare_managing_data.html",
    slug="business-development",
    download_url="https://www.dropbox.com/s/n61uasvfxr44uzu/Dimagi%27s%20BD%20Toolkit.zip?dl=1",
)
