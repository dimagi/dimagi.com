from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Cooperatives"
    ),
    summary=ugettext_lazy(
        "Mobile data collection's agriculture management applications provide real-time "
        "visibility into key data."
    ),
    template="data/sectors/content/agricultural_cooperatives.html",
    icon="svg/commcare/icon/agriculture.html",
    slug="agricultural-cooperatives",
    slides=[
        "data/sectors/content/agricultural_cooperatives/cooperative_farming.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Sector%20PDFs/CommCare_Agriculture.pdf",
    hubspot_form="4b3540e2-c7af-40df-8298-8bb543c766e6",
    thumbnail = "pages/sectors/agricultural-cooperatives/hero.jpg",
)


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Union des GIE des Producteurs de Céréale Local"
        ),
        country=countries.SENEGAL,
        description=ugettext_lazy("""
Dimagi is working with UGPCL to help better manage their cooperative of over 
1,000 farmers. Cooperative supervisors track the entire value-chain of 
small-scale farmers from the initial loan through its repayment, the output 
and quality of crops during the growing season, the farm produce’s contract
sale for processing, as well as value addition by third parties.
By providing a mobile-based system for tracking key metrics, cooperative 
managers can make informed decisions about the future of their cooperative, 
as well as estimate future cash flow requirements based on yield and sales data.
Examples of features in the application include tools to help farmers calculate 
planting density, step-by-step guidance that helps farmers prepare for harvest, 
GPS tracking, and a module with instructional videos about how to use the 
application.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "CARE"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
Care works to empower women in agriculture using technology.
        """),
        video_url="https://youtu.be/BPKpJ6vkHMw?list="
                  "PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
    ),
])
