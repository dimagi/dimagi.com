from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Education"
    ),
    summary=ugettext_lazy(
        "Support and improve farmer training programs with mobile data collection."
    ),
    template="data/sectors/content/education.html",
    theme="purple-theme",
    slug="education",
    slides=[
        "data/sectors/content/child_health/programs.html",
        "data/sectors/content/child_health/clinics.html",
        "data/sectors/content/child_health/patients.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Education.pdf",
    hubspot_form="520a0a36-354e-494b-b2e7-d4c842bee557",
    thumbnail = "pages/sectors/education/hero.jpg"
)
