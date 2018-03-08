from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project
from dimagi.sectors.data import areas, countries
from dimagi.data.case_studies import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "Child Health"
    ),
    summary=ugettext_lazy(
        "Use CommCare to monitor and improve antenatal, natal, and "
        "postnatal care."
    ),
    template="sectors/content/child_health.html",
    area=areas.HEALTH,
    slug="child-health",
    slides=[
        "sectors/content/child_health/programs.html",
        "sectors/content/child_health/clinics.html",
        "sectors/content/child_health/patients.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
)


SECTOR.add_case_studies([
    mhealth.lmrf_india.STUDY,
    mhealth.malaria_mozambique.STUDY,
    mhealth.tdh_burkinafaso.STUDY,
    mhealth.world_vision_motech.STUDY,
])


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Terre Des Hommes"
        ),
        country=countries.BURKINA_FASO,
        description=ugettext_lazy("""
Through funding from the Bill & Melinda Gates Foundation, Terre des 
Homes is deploying CommCare to 400 clinics in Burkina Faso to improve 
IMCI adherence. Terre des Hommes adopted the Integrated eDiagnostic 
Approach (IeDA) utilizing the Electronic Consultation Register (REC), 
a simple and low-cost IMCI diagnostic support tool to help nurses comply 
with IMCI protocols to ensure data accuracy. REC 2.0 is built on CommCare 
and includes both a tablet-based mobile app in addition to a web dashboard.
        """),
        video_url="https://www.youtube.com/watch?v=YS4NFMCwkm4&feature="
                  "youtu.be&list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
    ),
    Project(
        name=ugettext_lazy(
            "D-Tree International"
        ),
        country=countries.MALAWI,
        description=ugettext_lazy("""
D-Tree International designed a CommCare application while providing 
technical assistance to the USAID-funded “Integrated (HIV Effect) 
Migration and Positive Action for Community Transformation” (IMPACT) 
project. This project aims to improve the quality of life of orphans 
and vulnerable children in three target districts in Malawi. The 
application functions as a job aid to health surveillance assistants 
(HSAs), providing decision support to accurately treat sick children 
and follows Malawi’s government-designated IMCI protocol.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Malaria Consortium"
        ),
        country=countries.MOZAMBIQUE,
        description=ugettext_lazy("""
In collaboration with the London School of Hygiene and Tropical Medicine 
and University College of London, Malaria Consortium implemented inSCALE
to demonstrate that government-led Integrated Community Case Management
(iCCM) can improve healthcare services and expand coverage in Mozambique.
The project uses CommCare to strengthen communication between community
health workers (CHWs) and health facility supervisors, and with heavy
involvement of the Ministry of Health. InSCALE has the potential to expand
into other areas of the health system, with the goal of improved
diagnosis, treatment, and monitoring of disease throughout Mozambique.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "TulaSalud"
        ),
        country=countries.GUATEMALA,
        description=ugettext_lazy("""
TulaSalud’s mHealth program in Guatemala, KAWOK, uses CommCare for its
maternal and neonatal care application, in addition to others for
auxiliary nurse services, community surveying, and malaria monitoring
and treatment. Features include remote decision support, SMS alerts,
and local language customization, and incorporating open-source
products such as Google Earth for GPS tracking. A central function of
the app is to strengthen Guatemala’s Zero Hunger Pact to reduce chronic
and seasonal child malnutrition and child deaths among indigenous
communities.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "UNICEF"
        ),
        country=countries.MALAWI,
        description=ugettext_lazy("""
To improve access to protection services and reduce HIV’s impact for
women and children, UNICEF worked with the Malawi government to
established a Community Survivor Support Unit (CSSU) in Malawi’s
300 traditional authorities.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "World Vision"
        ),
        country=countries.NIGER,
        description=ugettext_lazy("""
World Vision has initiated an innovative IMCI mobile application
to increase integrated community case management (iCCM) and ensure
higher healthcare quality through job aids, referral support,
and supervision checklists. Mobile phones equipped with the
MOTECH suite are enabled with iCCM-specific modules. Job aids using
response-triggered decision tree algorithms will ensure adherence to
standardized protocols, improving diagnosis and treatment.
        """),
        video_url="https://www.youtube.com/watch?v=wuo0qoPQz0o&feature="
                  "youtu.be&list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
    ),
])
