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
    template="data/toolkits/summaries/managing_devices_ebook.html",
    slug="managing-devices-ebook",
    icon="svg/tookits/icons/managingdevices_scale.html",
    download_url="https://www.dropbox.com/s/lk5gujyrk3lm7v7/Managing%20Devices%20at%20Scale.pdf?dl=1",
    hubspot_form="186d64b8-8dcc-45d3-af92-03259efc96a8",
    hubspot_formId="61ca299b-1e89-4d2f-85b1-7ea182cf0170",
    icon="svg/case_management/broken_link.html",
)
