from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector
from dimagi.data.sectors import areas


SECTOR = Sector(
    name=ugettext_lazy(
        "Programmatic Research"
    ),
    summary=ugettext_lazy(
        "CommCare helps field-based studies increase efficiency, "
        "visibility, and scalability."
    ),
    template="sectors/content/programmatic_research.html",
    area=areas.DEVELOPMENT,
    slug="programmatic-research",
    slides=[
        "sectors/content/programmatic_research/core_functionalities.html",
        "sectors/content/programmatic_research/research_features.html",
        "sectors/content/programmatic_research/data_integrity.html",
        "sectors/content/programmatic_research/data_security.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/International%20research.pdf",
)
