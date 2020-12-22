from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "TechnoServe: Building an M&E Tools Suite"
    ),
    summary=[
        ugettext_lazy(
            "TechnoServe has worked to create impact in over 30 countries for "
            "more than 50 years. In the last 5 years, they have reached almost "
            "half a million beneficiaries across Latin America, Africa and India "
            "in multiple sectors, requiring an impressive combination of "
            "expertise and flexibility. "
        ),
        ugettext_lazy(
            "To service their projects’ M&E needs around the world, TechnoServe "
            "has re-organized its team structure and compiled a suite of "
            "products that allow them to capture, manage, and analyze data from "
            "an ever-changing set of indicators. A process, whose implementation "
            "could take six months or more, is now achievable in half that time."
        ),
    ],
    partners=[
        "TechnoServe",
    ],
    countries=[
        ugettext_lazy("Various (particular focus in Africa and Latin America)"),
    ],
    sectors=[
        ugettext_lazy("Agricultural Extension"),
        ugettext_lazy("Agricultural Logistics"),
        ugettext_lazy("Small Business"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Display Conditions"),
        ugettext_lazy("Validations Conditions"),
    ],
    slug="technoserve",
    primary_cta="6b77a5ff-69bd-468d-8ef0-19f48c5ab9ee",
    subnav_cta="46c4bb68-4b73-4889-8bb6-ee0354bb1dff",
    event_tracking_title="TechnoServe",
)
