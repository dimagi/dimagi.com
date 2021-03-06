from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector


SECTOR = Sector(
    name=ugettext_lazy(
        "Programmatic Research"
    ),
    summary=ugettext_lazy(
        "Mobile data collection helps field-based studies increase efficiency, "
        "visibility, and scalability."
    ),
    template="data/sectors/content/programmatic_research.html",
    slug="programmatic-research",
    theme="purple-theme",
    slides=[
        "data/sectors/content/programmatic_research/core_functionalities.html",
        "data/sectors/content/programmatic_research/research_features.html",
        "data/sectors/content/programmatic_research/data_integrity.html",
        "data/sectors/content/programmatic_research/data_security.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/International%20research.pdf",
    hubspot_form="0b2cd457-c95a-492f-8048-edc0a68a9e36",
    thumbnail = "pages/sectors/programmatic-research/hero.jpg",
)
