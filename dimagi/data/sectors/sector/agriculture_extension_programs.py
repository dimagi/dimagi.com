from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project, Resource
from dimagi.data.sectors import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Extension Programs"
    ),
    summary=ugettext_lazy(
        "Mobile technology can support farmer trainings, ensuring "
        "consistency in curriculum."
    ),
    template="data/sectors/content/agriculture_extension_programs.html",
    area=areas.AGRICULTURE,
    slug="agricultural-extension-programs",
    slides=[
        "data/sectors/content/agriculture_extension_programs/"
        "agricultural_extension_workers.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Agriculture%20Extension%20Programs.pdf",
)


SECTOR.add_projects([
    Sector(
        name=ugettext_lazy(
            "AG1"
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
            "AG2"
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
            "AG3"
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
            "AG4"
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


SECTOR.add_resources([
    Resource(
        url="https://www.commcarehq.org/exchange/"
            "145d386993f5b6cf40f1ba96bdb961a3/info/",
        name=ugettext_lazy("CARE CommCare App Available on the Exchange"),
    ),
    Resource(
        url="https://www.commcarehq.org/exchange/"
            "a8c0b7c6522fb4eeb707bc9f4123249e/info/",
        name=ugettext_lazy("Farmer Tracking App on the Exchange"),
    ),
    Resource(
        url="https://www.youtube.com/watch?v=UvdDOQOI2i4",
        name=ugettext_lazy(
            "CommCare Demo: CARE Pathways' Application for Agricultural "
            "Extension Workers"),
    ),
    Resource(
        url="https://www.youtube.com/watch?list="
            "PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr&v=8BzYVfsmmcA",
        name=ugettext_lazy(
            "Digitizing Development, CARE's Mobile MIS for Agriculture"),
    ),
    Resource(
        url="https://www.youtube.com/watch?v=uqRfAsuQx3s",
        name=ugettext_lazy("CommCare Demo on a Nokia"),
    ),
])
