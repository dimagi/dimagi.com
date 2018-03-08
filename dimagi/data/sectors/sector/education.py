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
    template="sectors/content/education.html",
    area=areas.DEVELOPMENT,
    slug="education",
    slides=[
        "sectors/content/education/performance_monitoring.html",
        "sectors/content/education/attendance_tracking.html",
        "sectors/content/education/standardized_assessments.html",
        "sectors/content/education/instructional_coaching.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Education.pdf",
)


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Save the Children"
        ),
        country=countries.THAILAND,
        description=ugettext_lazy("""
Save the Children Thailand created a CommCare application for School 
Monitoring that enrolls students in schools along the Thai-Myanmar 
border. The app keeps official enrollment records and tracks attendance 
and reasons for absenteeism. Students are visited at the beginning of 
the school year, at mid-year, and at end of the year to assess progress. 
Information from the app can also be used to create student ID cards, 
complete with photos of each individual student. The app was translated 
into multiple languages so it could be deployed in other regions. Dimagi 
trained the first 23 users and Save the Children is now scaling up to 
100 users.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "UNICEF"
        ),
        country=countries.GHANA,
        description=ugettext_lazy("""
UNICEF Ghana is using CommCare as an e-checklist to track and assess 
child-friendliness of schools around Ghana. The checklists monitor 
teacher and student attendance, assess facilities for safety and 
sanitation, track lesson plan adherence and classroom behavior, and 
compare results to a school’s past performance and community 
involvement. Field workers have the ability to enter data in real 
time for supervisors to assess schools’ performance on relevant 
indicators.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Anseye Pou Ayiti"
        ),
        country=countries.HAITI,
        description=ugettext_lazy("""
Anseye Pou Ayiti (Teach for Haiti) seeks to raise education outcomes 
in rural Haiti by recruiting, training, and equipping teacher-leaders 
to promote teacher excellence and student success. Their CommCare 
application enables pedagogical coaches to track teachers’ growth 
according to their individual professional growth plans and the 
organization’s competencies framework, and assists pedagogical 
coaches in conducting classroom observations and coaching sessions 
with teachers.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Bal Sansar: Taiyari"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
Bal Sansar is an organization that focuses on education and development 
for children and adolescents. As part of their “Taiyari” program, 
Bal Sansar is using CommCare to provide groups of adolescents with 
counselling on topics, such as: HIV, puberty, health, hygiene, and 
various social issues; and mobilizing these groups to tackle relevant 
social issues within their communities.
        """),
    ),
])
