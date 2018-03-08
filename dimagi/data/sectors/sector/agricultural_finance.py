from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Finance"
    ),
    summary=ugettext_lazy(
        "CommCare can help reduce the risks involved with microfinance."
    ),
    template="data/sectors/content/agricultural_finance.html",
    area=areas.AGRICULTURE,
    slug="agricultural-finance",
    slides=[
        "data/sectors/content/agricultural_finance/agricultural_finance.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Agricultural%20Finance.pdf",
)


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Micro Insurance Academy"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
Dimagi is launching a pilot with MIA to help with premiums calculations. 
Household members are registered and asset values are calculated 
programmatically, allowing for frontline workers to focus on providing 
counseling videos on claims coverage. Data collected is stored on CommCareHQ
to allow for swift payouts in the event of a claim. This system is designed
to expand into extremely low-resource settings while shifting claims 
management to an off-site, remote setting to reduce overhead expenditures.
        """),
    ),
])
