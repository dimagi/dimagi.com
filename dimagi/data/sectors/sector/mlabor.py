from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project, Resource
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "mLabor (Intrapartum Care)"
    ),
    summary=ugettext_lazy(
        "The CommCare Mobile Partograph app aims to reduce the "
        "partograph’s barriers."
    ),
    template="data/sectors/content/mlabor.html",
    slug="intrapartum-care",
    slides=[
        "data/sectors/content/mlabour/health_clinics_and_supervisors.html",
        "data/sectors/content/mlabour/intrapartum_care_providers.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Intrapartum%20Care.pdf",
)


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Mobile Partograph"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
Key alerts on urgent emergency action are sent to supervisors,
staff, and/or referral facilities, who can provide back-up advice
on appropriate next steps by making immediate phone calls to providers.
Monthly and quarterly reports are generated for health administrators
to assess labor monitoring, timely provision of care for abnormal labors,
and maternal and fetal health outcomes.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Human Development Innovation Fund"
        ),
        country=countries.TANZANIA,
        description=ugettext_lazy("""
In 2016 Dimagi was awarded an innovation grant from the
Human Development Innovation Fund (HDIF) in Tanzania.
Building on the success of mLabour in India, Dimagi will
leverage the HDIF grant to adapt mLabour to the Tanzanian
context and build upon its impact through two tracks:
Adaption & Validation and Diffusion.

Adaptation & Validation: Dimagi, in partnership with FHI 360
and other local research partners, will conduct focused
user-centered design activities and engage a wide range of
stakeholders to understand the requirements for scaling mLabour
throughout Tanzania. During the first year of the project,
Dimagi will conduct an initial 3-month study to validate the safety,
usability, and suitability of mLabour. In the second year,
additional studies will be conducted to assess how quality
of care is impacted through the use of mLabour.

Diffusion: Through the Diffusion Track,
Dimagi aims to deploy mLabour to five organizations in Tanzania,
spanning both the private and public sector.
Diffusion activities will include capacity building of two Tanzanian
technical organizations to support mLabour,
engagement with a range of private and public providers,
and engagement with the Ministry of Health and Social Welfare.
        """),
    ),
])


SECTOR.add_resources([
    Resource(
        url="http://www.grandchallenges.ca/2014/"
            "sustainable-cross-cultural-innovation-"
            "leads-to-safer-labour-and-delivery-of-newborns-in-india/",
        name=ugettext_lazy(
            "Sustainable cross-cultural innovation "
            "leads to safer labour and delivery of "
            "newborns in India"),
    ),
])
