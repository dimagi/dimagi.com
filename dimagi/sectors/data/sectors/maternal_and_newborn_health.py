from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project
from dimagi.sectors.data import areas, countries
from dimagi.case_studies.data import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "Maternal and Newborn Health"
    ),
    summary=ugettext_lazy(
        "Dimagi has worked on more MNH projects than in any other sector, "
        "including 58 projects globally."
    ),
    template="sectors/content/maternal_and_newborn_health.html",
    area=areas.HEALTH,
    slug="maternal-and-newborn-health",
    slides=[
        "sectors/content/maternal_and_newborn_health/maternal_and_newborn_health_programs.html",
        "sectors/content/maternal_and_newborn_health/health_workers.html",
        "sectors/content/maternal_and_newborn_health/health_facilities.html",
        "sectors/content/maternal_and_newborn_health/women_and_newborns.html",
    ],
    case_studies=[
        mhealth.lmrf_india.STUDY,
        mhealth.guatemala_childhealth.STUDY,
        mhealth.world_vision_motech.STUDY,
        mhealth.care_motech.STUDY,
    ],
    projects=[
        Project(
            name=ugettext_lazy(
                "Reducing Maternal and Newborn Deaths "
                "(ReMiND) Project, Catholic Relief Services"
            ),
            country=countries.BURKINA_FASO,
            description=ugettext_lazy("""
    The ReMiND project in Uttar Pradesh, India is well known as a leading 
    example of best practices for using mobile health technology to increase 
    key maternal and newborn health practices. Through ReMIND, Catholic Relief
    Services (CRS) and Dimagi are using CommCare to help Accredited Social 
    Health Activists (ASHAs) counsel and evaluate women and their newborns 
    for danger signs both before and after birth. Case management allows ASHAs
    to register and track every pregnant patient through pregnancy to the 
    postpartum period, as well as the newborns through their first year of life.
    Over 200 ASHAs have been trained to use these applications, ultimately 
    reaching over 20,000 women and their children.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None,
        ),
        Project(
            name=ugettext_lazy(
                "Better Birth, The Harvard School of Public Health"
            ),
            country=countries.MALAWI,
            description=ugettext_lazy("""
    The Harvard School of Public Health, in collaboration with the Indian government, 
    the World Health Organization, the Gates Foundation and Population Services International, 
    aims to assess whether the introduction of the WHO Safe Childbirth Checklist results 
    in a decline of maternal and newborn deaths. Outcomes of 172,000 births will be tracked, 
    in addition to the provision of essential supplies for safe birth. Dimagi is supporting 
    the research data collection process through CommCare and CommCareHQ, where managers, 
    supervisors, and researchers on the Better Birth Project will be able to access and 
    analyze submitted data.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None,
        ),
        Project(
            name=ugettext_lazy(
                "mHMtaani: Mobile Health for Our Communities, USAID"
            ),
            country=countries.MOZAMBIQUE,
            description=ugettext_lazy("""
    Under the APHIAplus project in Kenya, Pathfinder, with the support of USAID, 
    has worked with Dimagi to monitor and track the health of pregnant mothers 
    and orphans and vulnerable children. Using CommCare, CHWs are better able to 
    monitor maternal and newborn health indicators, keep women informed of their 
    expected delivery date and signs of complications, and help women prepare for 
    delivery. As of spring 2014, over 260 CHWs trained through mHMtaani were using 
    CommCare. The application also contributed to an increased number of facility-based 
    deliveries as a result of due date reminders.
            """),
            video_url="https://youtu.be/GUa7KW8s1VI?list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
            published_study_url=None,
            commcare_app_url=None,
        ),
        Project(
            name=ugettext_lazy(
                "Deploying MOTECH Suite to Support Global MNCH and Nutrition Programs, World Vision"
            ),
            country=countries.GUATEMALA,
            description=ugettext_lazy("""
    In partnership with Dimagi and the Grameen Foundation, World Vision has deployed 
    the MOTECH Suite for maternal, newborn, and child health (MNCH) and nutrition 
    mobile applications in ten countries, including Afghanistan, Burundi, India, 
    Indonesia, Mozambique, Niger, Sierra Leone, Sri Lanka, Uganda, and Zambia. 
    These applications are designed to support CHWs to deliver MNCH and nutrition 
    services more efficiently by reinforcing intervention protocols, serving as job 
    aids and acting as monitoring tools.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None,
        ),
        Project(
            name=ugettext_lazy(
                "mSante mHealth Project, Pathfinder"
            ),
            country=countries.NIGER,
            description=ugettext_lazy("""
    Pathfinder International, in collaboration with Dimagi, USAID, and the Haitian Ministry, 
    has trained more than 300 CHWs under the mSante mHealth Project. This mobile application 
    focuses on case management, health service delivery, referrals for tracking patients 
    between home and the health facility, and features modules focused on interventions 
    targeted at family planning and maternal and child health. Pathfinder and partners are 
    currently working toward scaling this project to the national level.
            """),
            video_url="https://youtu.be/wuo0qoPQz0o?list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
            published_study_url=None,
            commcare_app_url=None,
        ),
    ],
)
