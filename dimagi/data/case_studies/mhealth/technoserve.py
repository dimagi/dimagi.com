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
            "expertise and flexibility. To service their projects’ M&E needs "
            "around the world, TechnoServe has re-organized its team structure "
            "and compiled a suite of products that allow them to capture, manage, "
            "and analyze data from an ever-changing set of indicators. A process, "
            "whose implementation could take six months or more, is now achievable "
            "in half that time."
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
    download_url="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20TechnoServe%20Case%20Study.pdf",
    hubspot_form="78ddf7e9-5c96-4796-a895-3fad6b535963",
)
