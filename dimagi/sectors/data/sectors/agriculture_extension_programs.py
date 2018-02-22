from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project
from dimagi.sectors.data import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Extension Programs"
    ),
    summary=ugettext_lazy(
        "Mobile technology can support farmer trainings, ensuring consistency in curriculum."
    ),
    template="sectors/content/agriculture_extension_programs.html",
    area=areas.AGRICULTURE,
    slug="agriculture-extension-programs",
    slides=[
        "sectors/content/agriculture_extension_programs/agricultural_extension_workers.html",
    ],
    case_studies=[],
    projects=[
        Project(
            name=ugettext_lazy(
                "CARE Pathways, India, Tanzania"
            ),
            country=countries.TANZANIA,
            description=ugettext_lazy("""
    Since 2013, Dimagi has been working on the CARE Pathways project, 
    which is focused on helping female self-help agricultural groups 
    improve their productivity and increase incomes. Dimagi has set up
    a custom, tablet based scheduling and activity tracking system for 
    CARE’s extension workers, providing a “Knowledge Base” for on-site 
    refresher training, as well as a complex data collection system to 
    track group and individual performance on yield, income, and 
    empowerment indicators. All content is locally contextualized and 
    summarized in easily parsed custom reporting.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None
        ),
        Project(
            name=ugettext_lazy(
                "Catholic Relief Services"
            ),
            country=countries.INDIA,
            description=ugettext_lazy("""
    Catholic Relief Services is using CommCare to support an agriculture 
    project in India through the Gates Foundation’s initiative: Improved 
    Rice-based Rainfed Agricultural Systems. This tests the extension 
    agents and supervisors to track the progress of farms growing these 
    various varieties of rice. Each rice variety’s effectiveness is tracked
    and evaluated, leading to better livelihood outcomes in this 
    agriculturally dependent region.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None
        ),
        Project(
            name=ugettext_lazy(
                "Vaagdhara"
            ),
            country=countries.INDIA,
            description=ugettext_lazy("""
    Vaagdhara has developed an application using CommCare to monitor fruit 
    orchards. The application includes functionalities to select a village 
    for the project, register the farmer, plan, plantation counseling, and 
    conducts harvest monitoring for fruits, forestry trees, and intercrops.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None
        ),
        Project(
            name=ugettext_lazy(
                "Technoserve: AgriPlus"
            ),
            country=countries.SOUTH_AFRICA,
            description=ugettext_lazy("""
    Technoserve supports agriculture extension workers and supervisors to 
    track crop status, financials, and payroll information. The CommCare 
    application records farmer information for easy access by extension 
    workers and contains multimedia counseling materials such as the safe 
    use of pesticides and seedling growing techniques.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None
        ),
    ],
)
