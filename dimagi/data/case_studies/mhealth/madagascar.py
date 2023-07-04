from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "ACCESS Madagascar: Improving Health Outcomes in Remote and Low "
        "Connectivity Settings with CommCare"
    ),
    summary=[
        ugettext_lazy(
            "The Accessible Continuum of Care and Essential Services Sustained "
            "(ACCESS) program is a five-year project funded by USAID, led by "
            "Management Sciences for Health (MSH) and dedicated to strengthening "
            "Madagascar’s health system."
        ),
    ],
    summary_list_description=ugettext_lazy(
        "The goal of the project is to accelerate sustainable health impacts "
        "for the Malagasy population through three primary objectives:"
    ),
    summary_list=[
        ugettext_lazy(
            "Quality health services are sustainably available and accessible "
            "to all Malagasy communities in the program’s target regions"
        ),
        ugettext_lazy(
            "Health systems function effectively to support quality service delivery"
        ),
        ugettext_lazy(
            "The Malagasy people sustainably adopt health behaviors and social norms"
        ),
    ],
    summary_after_list=[
        ugettext_lazy(
            "Since 2016, the program has been using CommCare in order to improve "
            "the quality of services by adapting the Madagascar Ministry of Public "
            "Health (MOPH) paper-based forms to facilitate patient support and "
            "decision making, as well as provide job aids, counseling and disease "
            "classification tools."
        ),
    ],
    partners=[
        "Ministry of Public Health of Madagascar",
        "Management Sciences for Health (MSH)",
        "USAID"
    ],
    countries=[
        ugettext_lazy("Madagascar"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Healthcare"),
        ugettext_lazy("Family Planning"),
    ],
    features=[
        ugettext_lazy("DHIS2 Integration"),
        ugettext_lazy("SMS Functionality"),
    ],
    slug="access-madagascar",
    primary_cta="18e78896-eb76-4a82-886f-ee079588e4b8",
    subnav_cta="cfdb01ba-6950-40d2-9c59-865015b44313",
    event_tracking_title="ACCESS Madagascar",
    theme = "orange-theme",
)
