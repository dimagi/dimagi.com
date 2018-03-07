from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project, Resource
from dimagi.sectors.data import areas, countries
from dimagi.case_studies.data import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "Logistics & Supply Chain Management"
    ),
    summary=ugettext_lazy(
        "CommCare Supply is designed to inform and empower supervisors "
        "and supply officers with key supply information."
    ),
    template="sectors/content/logistics.html",
    area=areas.DEVELOPMENT,
    slug="logistics",
    slides=[
        "sectors/content/logistics/frontline_workers.html",
        "sectors/content/logistics/supply_officers.html",
        "sectors/content/logistics/organizations.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Logistics.pdf",
)


SECTOR.add_case_studies([
    mhealth.supply_chain_ghana.STUDY,
    mhealth.supply_chain_tanzania.STUDY,
    mhealth.supply_chain_malawi.STUDY,
])


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "ILSGateway"
        ),
        country=countries.TANZANIA,
        description=ugettext_lazy("""
The Ministry of Health (MoH) in Tanzania, with support from JSI 
through the USAID | DELIVER PROJECT has deployed the ILSGateway 
on a national scale, with over 4,600 Tanzanian facilities active 
today. In Tanzania, 93% of facilities are reportedly counting 
stock and managing bin cards more regularly and 97% of facilities 
are submitting requisition reports more regularly. 82% of districts 
reported improved visibility into tracer commodities. Users 
responding to the pilot evaluation in Tanzania indicated that 
the increased recognition and real-time nature of the SMS system 
was as powerful an incentive as monetary rewards, and reporting 
rates for the pilot were comparable with other systems that provided 
a monetary reward for reporting, demonstrated the feasibility of 
maintaining high and consistent user reporting rates without the 
need for supplementary monetary incentives.
        """),
        video_url="https://www.youtube.com/watch?v=skedLjDZRw8&feature=youtu.be",
    ),
    Project(
        name=ugettext_lazy(
            "Early Warning System"
        ),
        country=countries.GHANA,
        description=ugettext_lazy("""
The EWS system was designed to provide real-time stock status 
information on reproductive health commodities to decision-makers 
at all levels and to provide early warning of a drop in supplies.
        """),
        video_url="https://www.youtube.com/watch?v=fz5prbSQUyQ&feature=youtu.be",
    ),
    Project(
        name=ugettext_lazy(
            "cStock"
        ),
        country=countries.MALAWI,
        description=ugettext_lazy("""
The cStock system is scaled nationally to calculate just-in-time stock needs 
of the over 3,000 community health workers (CHWs) in Malawi as part of the 
Bill & Melinda Gates Foundation-funded JSI Supply Chains for Community Case 
Management (SC4CCM) initiative. In Malawi, CHWs provide Community Case 
Management (CCM), carrying and prescribing a defined list of essential 
medicines such as Oral Rehydration Salts, anti-malarials, antibiotics, 
and family planning commodities.  Built on CommCare Supply, cStock allows 
CHWs to use their personal phones to submit SMS with stock information, 
allowing community level data, previously unavailable, to be visible to 
decision makers at all levels of the system. A recent paper in the Journal 
of Global Health found that the use of cStock in Malawi contributed to 
significant reductions in stockout rates and lead times for resupply, 
as well as improvements in overall stock management [Shieshia, 2014].
        """),
    ),
])


SECTOR.add_resources([
    Resource(
        url="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4267094/",
        name=ugettext_lazy(
            "Strengthening community health supply chain performance "
            "through an integrated approach: Using mHealth technology "
            "and multilevel teams in Malawi"),
    ),
])
