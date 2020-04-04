from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "ILSGateway: CommCare for Improving the Supply Chain"
    ),
    summary=ugettext_lazy(
        "The Tanzanian Ministry of Health and Social Welfare created "
        "ILSGateway to monitor the supply of lifesaving medication at health "
        "facilities throughout Tanzania. After struggling with delays in "
        "stock tracking and requisition submissions, their new application "
        "expands the accessibility and visibility of logistics data and "
        "informs supply chain decision-making. The app monitors a set of "
        "tracer commodities, family planning and anti-malarial medications, "
        "and worker performance."
    ),
    partners=[
        "USAID",
        "Tanzania Ministry of Health and Social Welfare",
        "John Snow, Inc.",
    ],
    countries=[
        ugettext_lazy("Tanzania"),
    ],
    sectors=[
        ugettext_lazy("Infectious Disease"),
        ugettext_lazy("Maternal & Child Health"),
    ],
    features=[
        ugettext_lazy("Data Collection"),
        ugettext_lazy("Referrals"),
        ugettext_lazy("SMS Reminders"),
        ugettext_lazy("Custom Reports"),
    ],
    slug="mhealth-supply-chain-tanzania",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20ILSGateway%20Case%20Study.pdf",
    hubspot_form="95287374-5948-49e2-b67f-64e25723c355",
)
