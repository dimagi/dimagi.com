from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Sector, Project
from dimagi.sectors.data import areas, countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Agricultural Cooperatives"
    ),
    summary=ugettext_lazy(
        "CommCare's agriculture management applications provide real-time visibility into key data."
    ),
    template="sectors/content/agricultural_cooperatives.html",
    area=areas.AGRICULTURE,
    slug="agricultural-cooperatives",
    slides=[
        "sectors/content/agricultural_cooperatives/cooperative_farming.html",
    ],
    case_studies=[],
    projects=[
        Project(
            name=ugettext_lazy(
                "Union des GIE des Producteurs de Céréale Local"
            ),
            country=countries.SENEGAL,
            description=ugettext_lazy("""
    Dimagi is working with UGPCL to help better manage their cooperative of over 1,000 farmers.
    Cooperative supervisors track the entire value-chain of small-scale farmers from the initial
    loan through its repayment, the output and quality of crops during the growing season,
    the farm produce’s contract sale for processing, as well as value addition by third parties.
    By providing a mobile-based system for tracking key metrics, cooperative managers can
    make informed decisions about the future of their cooperative, as well as estimate future
    cash flow requirements based on yield and sales data.
    Examples of features in the application include tools to help farmers calculate planting density,
    step-by-step guidance that helps farmers prepare for harvest, GPS tracking,
    and a module with instructional videos about how to use the application.
            """),
            video_url=None,
            published_study_url=None,
            commcare_app_url=None,
        ),
        Project(
            name=ugettext_lazy(
                "CARE"
            ),
            country=countries.INDIA,
            description=ugettext_lazy("""
    Care works to empower women in agriculture using technology.
            """),
            video_url="https://youtu.be/BPKpJ6vkHMw?list=PLVmwIEfrcKqnGhas9Vy4CmPEvG9xVvQdr",
            published_study_url=None,
            commcare_app_url=None,
        ),
    ],
)
