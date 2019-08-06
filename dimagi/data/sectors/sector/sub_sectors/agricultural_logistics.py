from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Logistics"
    ),
    summary=ugettext_lazy(
        "Manage input distribution, cold chain of perishable goods, "
        "and warehouse receipt systems at lower cost with the support of CommCare."
    ),
    template="data/sectors/content/agricultural_logistics.html",
    icon="svg/commcare/icon/agriculture.html",
    slug="agricultural-logistics",
    slides=[
        "data/sectors/content/agricultural_logistics/value-chain-logistics.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Sector%20PDFs/CommCare_Agriculture.pdf",
    hubspot_form="72f11789-5d29-4ff2-943c-c05057436426",
)


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Smallholder Alliance for Sorghum"
        ),
        country=countries.HAITI,
        description=ugettext_lazy("""
In 2016, Dimagi helped to launch SMASH Mobil, an integrated mobile technology 
and reporting system designed to strengthen the sorghum supply chain in Haiti.
The SMASH Mobil system helps actors across the value chain use data capture 
and analytics to effectively manage agricultural extension and logistics activities, 
including crop monitoring, yield projections, purchasing, transport, conditioning, 
and inventory management.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "World Food Program"
        ),
        country=countries.ZAMBIA,
        description=ugettext_lazy("""
Dimagi has been running several trials of food distribution programs for rural 
schools in Zambia. CommCare has been deployed to link schools to grain and cooking 
oil silos. Teachers send an SMS stating their attendance levels over a period, 
as well as on-hand levels of cooking oils and grain. CommCare is able to calculate 
consumption rates based on this data, alerting silo managers to when particular 
schools will require a resupply and at what levels. The instantaneous nature of 
data processing ensures neither wastage nor under-supply of commodities for the 
nearly 5000 children in 88 schools that rely on this program for food.
        """),
    ),
])
