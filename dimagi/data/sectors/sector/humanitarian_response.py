from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector
from dimagi.data.sectors import areas


SECTOR = Sector(
    name=ugettext_lazy(
        "Humanitarian Response"
    ),
    summary=ugettext_lazy(
        "Quickly organize and share data during humanitarian crises with "
        "the help of mobile data collection apps."
    ),
    template="data/sectors/content/humanitarian_response.html",
    area=areas.RESPONSE,
    slug="humanitarian-response",
    slides=[
        "data/sectors/content/humanitarian_response/"
        "humanitarian_response_organizations.html",
        "data/sectors/content/humanitarian_response/"
        "frontline_workers.html",
        "data/sectors/content/humanitarian_response/"
        "beneficiaries_affected_by_crisis.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Humanitarian%20Response.pdf",
)



SECTOR.add_projects([
    Sector(
        name=ugettext_lazy(
            "HR1"
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
            "HR2"
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
