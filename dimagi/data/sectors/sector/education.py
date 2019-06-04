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
