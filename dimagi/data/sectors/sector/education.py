from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Education"
    ),
    summary=ugettext_lazy(
        "CommCare can help educational organizations gain visibility into "
        "what’s working and what’s not."
    ),
    template="data/sectors/content/education.html",
    area=areas.DEVELOPMENT,
    slug="education",
    slides=[
        "data/sectors/content/education/performance_monitoring.html",
        "data/sectors/content/education/attendance_tracking.html",
        "data/sectors/content/education/standardized_assessments.html",
        "data/sectors/content/education/instructional_coaching.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Education.pdf",
)


SECTOR.add_projects([
    Sector(
        name=ugettext_lazy(
            "EDU1"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        template="data/sectors/content/child_health.html",
        area=areas.DEVELOPMENT,
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
            "EDU2"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        template="data/sectors/content/child_health.html",
        area=areas.DEVELOPMENT,
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
            "EDU3"
        ),
        summary=ugettext_lazy(
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        template="data/sectors/content/child_health.html",
        area=areas.DEVELOPMENT,
        slug="child-health",
        slides=[
            "data/sectors/content/child_health/programs.html",
            "data/sectors/content/child_health/clinics.html",
            "data/sectors/content/child_health/patients.html",
        ],
        download_url="https://cdn2.hubspot.net/hubfs/503070/Child%20Health.pdf",
    ),
])
