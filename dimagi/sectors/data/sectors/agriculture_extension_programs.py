from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project, Resource
from dimagi.sectors.data import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Extension Programs"
    ),
    summary=ugettext_lazy(
        "Mobile technology can support farmer trainings, ensuring "
        "consistency in curriculum."
    ),
    template="sectors/content/agriculture_extension_programs.html",
    area=areas.AGRICULTURE,
    slug="agriculture-extension-programs",
    slides=[
        "sectors/content/agriculture_extension_programs/"
        "agricultural_extension_workers.html",
    ],
)


SECTOR.add_projects([
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
