from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Improving Integrated Community Case Management in Mozambique"
    ),
    summary=ugettext_lazy(
        "The inSCALE project seeks to demonstrate that government-led "
        "Integrated Community Case Management (iCCM) can improve "
        "healthcare services and expand coverage in Mozambique, "
        "a country where only 52% of the population has healthcare "
        "coverage. The project adopted CommCare and CommConnect to "
        "strengthen communication between community health workers "
        "(CHWs) and health facility supervisors, and with heavy "
        "involvement of the Ministry of Health, inSCALE has the potential "
        "to expand into other areas of the health system, with the "
        "goal of improved diagnosis, treatment, and monitoring of disease "
        "throughout Mozambique."
    ),
    partners=[
        "Malaria Consortium",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("Mozambique"),
    ],
    sectors=[
        ugettext_lazy("child health"),
        ugettext_lazy("pneumonia"),
        ugettext_lazy("malaria"),
        ugettext_lazy("iCCM"),
    ],
    features=[
        ugettext_lazy("active data management"),
        ugettext_lazy("decision & diagnostic support"),
        ugettext_lazy("respiratory rate counter"),
        ugettext_lazy("motivational messages (for CHWs & Supervisors)"),
        ugettext_lazy("case management"),
        ugettext_lazy("multimedia"),
        ugettext_lazy("custom reporting"),
    ],
    slug="mhealth-malaria-mozambique",
    download_url="https://www.dropbox.com/s/trffquc2e3ra0gw/mhealth-malaria-mozambique.pdf?dl=1",
    hubspot_form="e39f88d8-e985-44bd-92ff-48a382bed12b",
)
