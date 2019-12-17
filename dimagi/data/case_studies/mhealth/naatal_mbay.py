from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Naatal Mbay: CommCare for Agricultural Support"
    ),
    summary=ugettext_lazy(
        "Naatal Mbay, which means “making agriculture prosperous,” is a Feed "
        "the Future project that uses digital tools to empower farmer-serving "
        "organizations active in the rice, maize, and millet value chains in "
        "Senegal. The program uses CommCare to track inputs and productivity, "
        "manage loans, and collect rainfall data. CommAgri, Naatal Mbay’s digital "
        "tool, is used by 55 cooperatives and 500 extension agents, who have "
        "registered 68,000 farmers."
    ),
    partners=[
        "RTI",
        "Feed the Future",
        "USAID",
    ],
    countries=[
        ugettext_lazy("Senegal"),
    ],
    sectors=[
        ugettext_lazy("Agricultural Cooperatives"),
        ugettext_lazy("Agricultural Logistics"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("CommCare Supply"),
        ugettext_lazy("Area Mapper"),
    ],
    slug="naatal-mbay",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20Naatal%20Mbay%20Case%20Study.pdf",
    hubspot_form="2f9b7c9b-1723-4273-87ff-487d6b5d0564",
    download_url_language="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20Naatal%20Mbay%20Case%20Study_French.pdf",
    hubspot_form_language="e2e24018-df22-400a-9d05-ea207fc89db5",
)
