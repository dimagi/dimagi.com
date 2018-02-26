from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project, Resource
from dimagi.sectors.data import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Gender Based Violence"
    ),
    summary=ugettext_lazy(
        "Learn how CommCare can help address gender-based violence issues."
    ),
    template="sectors/content/gender_based_violence.html",
    area=areas.DEVELOPMENT,
    slug="gender_based_violence",
    slides=[
        "sectors/content/gender_based_violence/gender_based_violence.html",
        "sectors/content/gender_based_violence/frontline_workforce.html",
        "sectors/content/gender_based_violence/beneficiaries.html",
    ],
    case_studies=[],
    projects=[
        Project(
            name=ugettext_lazy(
                "USAID Innovative Uses of Mobile Technology to Improve GBV Services"
            ),
            country=countries.INDIA,
            description=ugettext_lazy("""
    Since Sept 2013, Dimagi has been collaborating with its partners St. John’s 
    Research Institute to apply CommCare to help auxiliary nurses and other 
    health workers identify and manage cases of GBV. CommCare helps the health 
    workers follow tested, standardized protocols and inform survivors of their 
    rights and options, provide counseling messages, and facilitate support services. 
    CommCare reduces the burden of paper-based reporting and increases adherence to 
    tested protocols that accurately screen for GBV.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None
        ),
        Project(
            name=ugettext_lazy(
                "UNICEF Community Survivor Support Unit Teams"
            ),
            country=countries.MALAWI,
            description=ugettext_lazy("""
    In an effort to improve access to woman and child protection services and reduce the 
    impact of HIV on women and children, UNICEF worked with the government of Malawi 
    established a Community Victim Support Unit (CVSU) in each of the 300 authorities 
    in the country. CVSUs provide psychosocial support, mediation, and referral services 
    for women and children survivors of abuse, violence, exploitation, and neglect. 
    CommCare has been used to strengthen monitoring and support the activities and 
    information systems of CVSUs.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None
        ),
    ],
    additional_resources=[
        Resource(
            url="https://www.youtube.com/watch?v=HSm-9PZaPFs",
            name="Gender-Based Violence and Innovative Technologies",
        ),
    ],
)
