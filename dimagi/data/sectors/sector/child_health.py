from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import areas, countries
from dimagi.data.case_studies import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "Health Care Delivery"
    ),
    summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
    ),
    template="data/sectors/content/child_health.html",
    area=areas.HEALTH,
    slug="child-health",
    slides=[
        "data/sectors/content/child_health/programs.html",
        "data/sectors/content/child_health/clinics.html",
        "data/sectors/content/child_health/patients.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
)


SECTOR.add_projects([
    Sector(
        name=ugettext_lazy(
            "CH1"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        template="data/sectors/content/child_health.html",
        area=areas.HEALTH,
        slug="child-health",
        slides=[
            "data/sectors/content/child_health/programs.html",
            "data/sectors/content/child_health/clinics.html",
            "data/sectors/content/child_health/patients.html",
        ],
        download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
    ),
    Sector(
        name=ugettext_lazy(
            "CH2"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        template="data/sectors/content/child_health.html",
        area=areas.HEALTH,
        slug="child-health",
        slides=[
            "data/sectors/content/child_health/programs.html",
            "data/sectors/content/child_health/clinics.html",
            "data/sectors/content/child_health/patients.html",
        ],
        download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
    ),
    Sector(
        name=ugettext_lazy(
            "CH3"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        template="data/sectors/content/child_health.html",
        area=areas.HEALTH,
        slug="child-health",
        slides=[
            "data/sectors/content/child_health/programs.html",
            "data/sectors/content/child_health/clinics.html",
            "data/sectors/content/child_health/patients.html",
        ],
        download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
    ),
])


SECTOR.add_case_studies([
    mhealth.lmrf_india.STUDY,
    mhealth.malaria_mozambique.STUDY,
    mhealth.tdh_burkinafaso.STUDY,
    mhealth.world_vision_motech.STUDY,
])
