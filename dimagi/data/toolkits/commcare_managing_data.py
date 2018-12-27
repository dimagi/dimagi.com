from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Managing Data in CommCare"
    ),
    tagline=ugettext_lazy(
        "A starter guide to inspecting, cleaning and exporting data in "
        "CommCare."
    ),
    template="data/toolkits/summaries/commcare_managing_data.html",
    slug="commcare-managing-data",
    download_url="https://www.dropbox.com/s/lguz3gth6kovw62/M%26E%20Starter%20Guide.pdf?dl=1",
    hubspot_form="f59879b3-23cb-41a6-b4f8-e1daa8ba4141",
    hubspot_formId="7ad4227e-5f4a-4c39-bd87-bfa2151019cb",
    icon="svg/case_management/broken_link.html",
)
