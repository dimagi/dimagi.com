from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Healthy Mother, Healthy Baby (HMHB), "
        "Digitally Transforming Service Delivery in Tajikistan"
    ),
    summary=[
        ugettext_lazy(
            "The USAID-funded Healthy Mother, Healthy Baby (HMHB) Activity set out "
            "to improve health outcomes in Tajikistan through digital transformation. "
            "It expands USAID’s maternal, newborn, and child health (MNCH) and nutrition "
            "investments in Tajikistan as the country introduces new health strategies. "
            "It is a multi-year activity with a mandate to make sustainable improvements "
            "in the ability of the Government of Tajikistan to deliver quality maternal "
            "and child health and nutrition services. It focuses on building the technical "
            "capacity, leadership, and management of Tajikistan while also creating a "
            "path towards country-wide digitalization and policy reform."
        ),
        ugettext_lazy(
            "Healthy Mother, Healthy Baby aims to improve the quality of healthcare, "
            "increase access to health services, and help meet the increasing demand "
            "for health services in 12 districts. It will build the capacity of health "
            "providers through in-service training and ongoing continuing education; "
            "integrate person-centered care across hospitals, Primary Health Care (PHC), "
            "and Healthy lifestyle centers (HLSCs); and support an enabling environment "
            "for skilled, motivated providers by expanding Quality Improvement (QI) "
            "efforts and availability of infrastructure and equipment."
        ),
        ugettext_lazy(
            "HMHB leverages the power of CommCare, to create an enabling environment "
            "to strengthen capacity and ensure users have the correct information at "
            "their fingertips to make better-informed decisions."
        ),
    ],
    partners=[
        "Ministry of Health and Social Protection of the Population (MOHSSP)",
        "USAID",
        "Abt Associates"
    ],
    countries=[
        ugettext_lazy("Khatlon Province"),
        ugettext_lazy("Tajikistan"),
    ],
    sectors=[
        ugettext_lazy("Maternal and Child Nutrition and Health"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Survey Application"),
        ugettext_lazy("Decision Support"),
        ugettext_lazy("Attendance Tracker"),
        ugettext_lazy("Facility Assessment"),
        ugettext_lazy("Multimedia"),
        ugettext_lazy("Counseling"),
        ugettext_lazy("DHIS2 Integration"),
    ],
    slug="tajikistan",
    primary_cta="108146c4-e622-4606-ab7f-c0285d3e94b0",
    subnav_cta="c6b75596-0711-4589-a763-c7662c5f43e7",
    event_tracking_title="Healthy Mother, Healthy Baby (HMHB) Tajikistan",
)
