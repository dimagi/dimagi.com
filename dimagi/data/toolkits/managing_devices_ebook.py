from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Managing Devices at Scale"
    ),
    tagline=ugettext_lazy(
        "Key learnings from managing thousands of devices in a "
        "large-scale mobile health project."
    ),
    template="toolkits/summaries/managing_devices_ebook.html",
    slug="managing-devices-ebook",
    download_url="https://www.dropbox.com/s/lguz3gth6kovw62/M%26E%20Starter%20Guide.pdf?dl=1",
    hubspot_form="186d64b8-8dcc-45d3-af92-03259efc96a8",
)
