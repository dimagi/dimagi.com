from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project, Resource
from dimagi.sectors.data import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Ebola Response"
    ),
    summary=ugettext_lazy(
        "Improve core infectious disease response roles and help "
        "decrease the risk of future disease outbreaks."
    ),
    template="sectors/content/ebola_response.html",
    area=areas.HEALTH,
    slug="ebola-response",
    slides=[
        "sectors/content/ebola_response/surveillance.html",
        "sectors/content/ebola_response/sensitization.html",
        "sectors/content/ebola_response/adherence_to_screening.html",
        "sectors/content/ebola_response/diagnostics.html",
        "sectors/content/ebola_response/stock_tracking.html",
        "sectors/content/ebola_response/patient_self_reporting.html",
        "sectors/content/ebola_response/ebola_response_applications.html",
    ],
    case_studies=[],
    projects=[
        Project(
            name=ugettext_lazy(
                "The Earth Institute at Columbia University, UNFPA, Ministry of Health"
            ),
            country=countries.GUINEA,
            description=ugettext_lazy("""
    In Guinea, the Earth Institute, UNFPA, and the Guinean Ministry of Health have 
    adapted the standardized Ebola contact-tracing form to a CommCare application. 
    Available in both English and French, the application was designed to be quickly
    deployed, updated with changing protocols, and includes an instructional module 
    with videos that contact-tracers can view for post-training guidance. The Earth 
    Institute uses a dashboard developed by Tableau and also employs user-configurable
    reports that are viewable directly in CommCare. A pilot was deployed in December 
    2014 and has since scaled up to 5 of the 8 prefectures (Conakry, Coyah, Dubreka,
    Forecariah, and Boffa) that currently have Ebola, with 317 contact tracers and 
    50 supervisors on CommCare.
            """),
            video_url="https://www.youtube.com/watch"
                      "?v=_ksL_Jj6m5g&feature=youtu.be&list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
            published_study_url=None,
            commcare_app_url=None,
        ),
        Project(
            name=ugettext_lazy(
                "Innovations for Poverty Action"
            ),
            country=countries.SIERRA_LEONE,
            description=ugettext_lazy("""
    Together with the London School of Hygiene and Tropical 
    Medicine (LSHTM) and International Medical Corps (IMC), 
    IPA developed a two-armed cluster-randomized trial to 
    evaluate the effectiveness of a smartphone-based CommCare 
    data capture and management system relative to the current 
    paper-based system for Ebola contact tracing and monitoring 
    in Sierra Leone. The 11 chiefdoms in Port Loko district were 
    randomized to receive either the CommCare intervention or 
    the paper-based system control.
            """),
            video_url="https://www.youtube.com/watch"
                      "?v=csqO5t8svAU&feature=youtu.be&list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
            published_study_url=None,
            commcare_app_url=None,
        ),
    ],
    additional_resources=[
        Resource(
            url="http://www.ghspjournal.org/content/early/"
                "2015/11/12/GHSP-D-15-00207.full.pdf+html",
            name="Introduction of Mobile Health Tools to Support "
                 "Ebola Surveillance and Contact Tracing in Guinea",
        ),
        Resource(
            url="https://www.youtube.com/watch?v=e9Lff9rmFxA",
            name="Filling Out a Form: Contact Tracing App Demo (French)",
        ),
    ],
)
