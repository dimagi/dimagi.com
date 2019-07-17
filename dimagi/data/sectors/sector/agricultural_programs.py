from __future__ import absolute_import

from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Extension Programs"
    ),
    summary=ugettext_lazy(
        "Mobile technology can support farmer trainings, ensuring "
        "consistency in curriculum."
    ),
    icon="svg/sectors/agriculture/agriculture_programs.html",
    theme="green",
    slug="agricultural-programs",
)


SECTOR.add_sub_sectors([
    Sector(
        name=ugettext_lazy(
            "Agricultural Extension"
        ),
        summary=ugettext_lazy(
            "Support and improve farmer training programs with mobile data collection."
        ),
        icon="svg/sectors/agriculture/agricultural_extension_programs.html",
        theme="green-theme",
        slug="sector_agriculture_extension_programs",
        is_v2=True,
    ),
    Sector(
        name=ugettext_lazy(
            "Agricultural Finance"
        ),
        summary=ugettext_lazy(
            "Mitigate the risks associated with microfinance with mobile tools."
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
            "Manage input distribution, cold chain of perishable goods, and "
            "warehouse receipt systems at lower cost with mobile tools."
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
            "Mobile data collection's agricultural management apps provide "
            "real-time insight into key data."
        ),
        icon="svg/sectors/agriculture/agricultural_cooperatives.html",
        theme="green-theme",
        slug="agricultural-cooperatives",
    ),
])
