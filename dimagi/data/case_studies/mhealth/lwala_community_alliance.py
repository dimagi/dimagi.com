from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Lwala Community Alliance: CommCare for Improving Vaccination Rates"
    ),
    summary=[
        ugettext_lazy(
            "Lwala Community Alliance in Kenya fights high rates of maternal "
            "mortality and HIV. Using a community-led health model and a custom "
            "CommCare-based mobile application, Community Health Workers (CHWs) "
            "register each pregnant woman or child under five years old into the "
            "formal healthcare system. The application then walks the CHW through "
            "the proper workflows for vaccinations, family planning, disease "
            "diagnosis and treatment, or a number of other requested services. So "
            "far, the program has reached vaccination rates of over 95% across a "
            "population of 60,000 people."
        ),
    ],
    partners=[
        "Lwala Community Alliance",
        "Migori County Ministry of Health",
    ],
    countries=[
        ugettext_lazy("Kenya"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
        ugettext_lazy("Infectious Disease"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Referrals"),
        ugettext_lazy("Real-Time Decision Support"),
        ugettext_lazy("CHW Supervision"),
    ],
    slug="lwala-community-alliance",
    primary_cta="7f1f008a-1549-4a3a-bc17-f796f462797c",
    subnav_cta="670be0f6-7fe3-492e-9463-d5c827ecd3d9",
    event_tracking_title="Lwala Community Alliance",
)
