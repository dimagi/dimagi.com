from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project
from dimagi.sectors.data import areas, countries


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
    slug="international-research",
    slides=[
        "sectors/content/programmatic_research/core_functionalities.html",
        "sectors/content/programmatic_research/research_features.html",
        "sectors/content/programmatic_research/data_integrity.html",
        "sectors/content/programmatic_research/data_security.html",
    ],
    case_studies=[],
    projects=[],
    additional_resources=[],
)
