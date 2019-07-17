from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Tuberculosis"
    ),
    summary=ugettext_lazy(
        "Help build TB treatment capacity with CommCare."
    ),
    template="data/sectors/content/tuberculosis.html",
    slug="tuberculosis",
    slides=[
        "data/sectors/content/tuberculosis/tb_programs_and_clinics.html",
        "data/sectors/content/tuberculosis/health_workers.html",
        "data/sectors/content/tuberculosis/tb_patients.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Tuberculosis.pdf",
)

SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "The International Center for AIDS Care and Treatment "
            "Programs at Columbia University (ICAP)"
        ),
        country=countries.LESOTHO,
        description=ugettext_lazy("""
ICAP is using CommCare to improve treatment outcomes of TB patients and 
household contacts by strengthening their DOTS system and follow-up. 

Nurses use CommCare in government clinics to register TB patients, schedule 
appointments, and follow up on missed appointments. CHWs use CommCare during 
home visits to screen contacts for TB and refer potential cases to clinics. 
CommCare helps ICAP supervise DOTS supporters and provide TB education and 
counseling through multimedia.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "The International Union for TB and Lung Disease"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
In rural Jharkhand, Rural Health Care Providers (RHCP) and Lab Technicians (LT) use 
CommCare to improve TB case detection, follow-up rates, symptomatic case management, 
and DOTS adherence.

RHCP refers symptomatic cases to LT where sputum is tested for TB. If lost to follow up, 
an SMS is sent to the patient, RHCP, and LT. An SMS is also sent to the patient with 
lab results.
        """),
    ),
])
