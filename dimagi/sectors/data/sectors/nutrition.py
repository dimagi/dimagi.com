from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project
from dimagi.sectors.data import areas, countries
from dimagi.case_studies.data import mhealth


SECTOR = Sector(
    name=ugettext_lazy(
        "Nutrition"
    ),
    summary=ugettext_lazy(
        "Support a variety of nutrition programs with CommCare."
    ),
    template="sectors/content/nutrition.html",
    area=areas.HEALTH,
    slug="nutrition",
    slides=[
        "sectors/content/nutrition/nutrition_programs_and_organizations.html",
        "sectors/content/nutrition/frontline_workers.html",
        "sectors/content/nutrition/beneficiaries.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Nutrition.pdf",
)


SECTOR.add_case_studies([
    mhealth.lmrf_india.STUDY,
    mhealth.world_vision_motech.STUDY,
    mhealth.guatemala_childhealth.STUDY,
])


SECTOR.add_projects([
    Project(
        name=ugettext_lazy(
            "Real Medicine Foundation (RMF)"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
RMF implemented CommCare to assist Community Nutrition Educators (CNEs) 
in identifying children with Severe Acute Malnutrition (SAM) and Moderate 
Acute Malnutrition (MAM) through measuring MUAC. In addition to tracking 
MUAC over time, the application supports counseling to families of 
malnourished children and refers these children to government treatment 
facilities for rehabilitation in villages of Madhya Pradesh. Their work
was previously recorded in paper format and implementation of mobile 
data collection has reduced the latency period from 45 days to eight hours.
        """),
        published_study_url="https://www.microsoft.com/en-us/research/"
                            "people/cutrell/"
                            "?from=http%3A%2F%2Fresearch.microsoft.com"
                            "%2Fen-us%2Fum%2Fpeople%2Fcutrell"
                            "%2Fmedhi-nordichi2012-commcarecasestudy.pdf",
    ),
    Project(
        name=ugettext_lazy(
            "Society for Nutrition, Education and Health Action (SNEHA)"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
SNEHA implemented CommCare to replace its manual data collection and entry 
system to track mothers and newborns in Mumbai’s slums, accompanying a 
programmatic scale-up in strengthening referral linkages within the municipal 
health system. The CommCare application allows individual children’s weights 
to be updated on a monthly basis, and support the health worker to follow-up 
with malnourished children.
        """),
        commcare_app_url="https://www.commcarehq.org/exchange/"
                         "3fb6383acfdc9e726cb089fba4722ee2/info/"
                         "?__hstc=240960668.41b1f79d5eb5c17e0c46e4237991c19b."
                         "1518524627256.1518774288328.1518783005958.15"
                         "&__hssc=240960668.31.1518783005958"
                         "&__hsfp=2464441440",
    ),
    Project(
        name=ugettext_lazy(
            "World Vision, Africa, Southeast Asia, and the Middle East"
        ),
        country=countries.GLOBE,
        description=ugettext_lazy("""
World Vision is implementing a standard set of CommCare applications for 
nutrition in nine countries in Africa, Southeast Asia, and the Middle East. 
CommCare supports community health workers to regularly screen children for 
nutrition status and related illness, in addition immunization status. 
The application includes tools for GMP, PD/Hearth, and CMAM.
        """),
    ),
    Project(
        name=ugettext_lazy(
            "Food for the Hungry"
        ),
        country=countries.MOZAMBIQUE,
        description=ugettext_lazy("""
Food for the Hungry implemented CommCare to improve surveillance and 
counseling during GMP sessions in northern Cabo Delgado, a province with 
one of the highest malnutrition rates in Mozambique. The CommCare 
application calculates and records children’s weight-for-age Z scores and MUAC.
        """),
        video_url="https://youtu.be/YS4NFMCwkm4"
                  "?list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
    ),
    Project(
        name=ugettext_lazy(
            "Operation Smile"
        ),
        country=countries.INDIA,
        description=ugettext_lazy("""
Operation Smile implemented a CommCare application to track the nutritional 
status of children with cleft lip and palates in Assam. The application 
tracks the children’s progress in becoming sufficiently nourished to undergo 
cleft palate surgery.
        """),
        commcare_app_url="https://www.commcarehq.org/exchange/"
                         "8bd844d12202009cc17a03dc01d0cbaa/info/"
                         "?__hstc=240960668.08ee0e6075b9e3e4b1f3bcfe39a26c87."
                         "1477145574241.1477257909331.1477285607734.7"
                         "&__hssc=240960668.27.1477285607734&__"
                         "hsfp=4011894190",
    ),
])
