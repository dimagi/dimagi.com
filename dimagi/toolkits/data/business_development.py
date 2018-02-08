from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.toolkits.models import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Business Development Toolkit"
    ),
    tagline=ugettext_lazy(
        "Use the Business Development Toolkit to develop a BD pipeline "
        "for your organization"
    ),
    template="toolkits/summaries/business_development.html",
    slug="business-development",
    download_url="https://www.dropbox.com/s/n61uasvfxr44uzu/Dimagi%27s%20BD%20Toolkit.zip?dl=1",
)
