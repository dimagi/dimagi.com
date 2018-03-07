from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project, Resource
from dimagi.sectors.data import areas, countries
from dimagi.case_studies.data import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "HIV/AIDS"
    ),
    summary=ugettext_lazy(
        "Dimagi has significant experience working on HIV/AIDS"
        " projects in numerous countries and contexts."
    ),
    template="sectors/content/hiv_aids.html",
    area=areas.HEALTH,
    slug="hiv-aids",
    slides=[
        "sectors/content/hiv_aids/community_health_workers.html",
        "sectors/content/hiv_aids/clinics_and_clinicians.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/CommCare%20for%20HIVAIDS.pdf",
)


SECTOR.add_case_studies([
    mhealth.hiv_zimbabwe.STUDY,
])


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Global Solutions for Infectious Disease"
        ),
        country=countries.ZIMBABWE,
        description=ugettext_lazy("""
With support from Econet Wireless and the Zimbabwean Ministry of 
Health and Child Care, Global Solutions for Infectious Diseases 
(GSID) created a mobile system with Dimagi and ODK Diagnostics 
to better process rapid diagnostic tests for HIV and malaria. 
The system utilizes CommCare’s case management and reporting 
features to digitize health workers’ workloads, and ODK-Dx’s 
ability to process, analyze, and return RDT results with 
computer vision algorithms. The system was used in five sites 
in Manicaland province, including three hospitals and two health 
centers.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Brigham & Women’s Hospital, 14 countries in Africa,"
            " Asia, & the Americas"
        ),
        country=countries.GHANA,
        description=ugettext_lazy("""
Dimagi partnered with Boston’s Brigham and Women’s Hospital and 
Social & Scientific Systems, Inc. (SSS) to develop a scalable 
text messaging (SMS) system to improve HIV medication adherence 
in 14 countries in Africa, Asia, and the Americas. The SMS 
intervention is part of an ongoing clinical trial, A5288, 
supported by the Aids Clinical Trial Group (ACTG). The system 
was designed to optimize combination therapy for HIV-infected 
patients, who currently struggle with treatment and have 
demonstrated resistance to common anti-retroviral drugs.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "WITS Health Consortium-IMAGE"
        ),
        country=countries.SOUTH_AFRICA,
        description=ugettext_lazy("""
The IMAGE Project combines a microfinance intervention with a
gender and HIV awareness curriculum with the aim of 
improving the social and economic well-being of households 
and reducing the risk of HIV infection and gender-based 
violence. The IMAGE Project is currently working with 5000 
households in 300 rural villages across 4 South African 
provinces – Limpopo, Gauteng, Northwest and KwaZulu Natal. 
The nature of the program is highly decentralized – with 35 
field staff that work in small, dispersed teams. The project 
has additional replication sites in Tanzania, Kenya, 
Zimbabwe and Peru.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Médecins Sans Frontières"
        ),
        country=countries.SOUTH_AFRICA,
        description=ugettext_lazy("""
MSF tested a proof of concept CommCare App in the community 
of Khayelitsha, Cape Town to keep track of patients in ART 
Adherence Club (AC) clubs. By using the application, MSF 
staff would be able to track club attendance in real time,
make referrals to clinics, and identify defaulters. The 
system also enabled individual feedback to facilitators 
based on their mobile activity, and regular email reports 
of clubs activities available for M&E team, as well as 
raw data to identify and trigger alerts for high-risk or
defaulting clients
        """),
    ),
    Project(
        name=ugettext_lazy(
            "CARE"
        ),
        country=countries.SOUTH_AFRICA,
        description=ugettext_lazy("""
In South Africa, CARE provides Integrated Access to Care and 
Treatment (iACT) literacy programmes for registered clients 
in local communities. They are using CommCare to register 
participants and provide follow up services and education 
for both HIV and TB, including making client referrals to 
clinics, recording client attendance during iACT sessions, 
and schedule automatic reminders for client follow up.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "CommCare for Community Survivor Support Unit Teams"
        ),
        country=countries.MALAWI,
        description=ugettext_lazy("""
To improve access to protection services and reduce HIV\’s 
impact for women and children, UNICEF worked with the 
Malawi government to established a Community Survivor 
Support Unit (CSSU) in Malawi’s 300 traditional authorities. 
CSSUs provide psychosocial support, mediation, and referral 
services for women and children survivors of abuse, 
exploitation, and neglect. CommCare is strengthening 
CSSU monitoring, activities, and information systems.
        """),
    ),
])


SECTOR.add_resources([
    Resource(
        url="https://www.measureevaluation.org/resources/publications/sr-14-99",
        name=ugettext_lazy(
            "Nascimento, N., Cannon, M., Perales, N., Chariyeva, Z. "
            "Assessment of an mHealth initiative to improve patient "
            "retention. USAID, PEPFAR, Measure Evaluation. August 2014."),
    ),
])
