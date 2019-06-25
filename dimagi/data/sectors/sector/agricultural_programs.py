from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project, Resource
from dimagi.data.sectors import  countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Extension Programs"
    ),
    summary=ugettext_lazy(
        "Mobile technology can support farmer trainings, ensuring "
        "consistency in curriculum."
    ),
    icon="svg/sectors/agriculture/agriculture_programs.html",
    theme="green-theme",
    slug="agricultural-programs",
)


SECTOR.add_sub_sectors([
    Sector(
        name=ugettext_lazy(
            "Agricultural Extension"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        icon="svg/sectors/agriculture/agricultural_extension_programs.html",
        theme="green-theme",
        slug="agricultural-extension-programs",
    ),
    Sector(
        name=ugettext_lazy(
            "Agricultural Finance"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        icon="svg/sectors/agriculture/agricultural_finance.html",
        theme="green-theme",
        slug="agricultural-finance",
    ),
    Sector(
        name=ugettext_lazy(
            "Agricultural Logistics"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        icon="svg/sectors/agriculture/agricultural_logistics.html",
        theme="green-theme",
        slug="agricultural-logistics",
    ),
    Sector(
        name=ugettext_lazy(
            "Agricultural Cooperatives"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        icon="svg/sectors/agriculture/agricultural_cooperatives.html",
        theme="green-theme",
        slug="agricultural-cooperatives",
    ),
])
