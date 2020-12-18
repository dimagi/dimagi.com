from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "SMASH Mobil: CommCare for Improving Local Supply Chains"
    ),
    summary=[
        ugettext_lazy(
            "In 2013, the Brasserie Nationale d’Haïti (BRANA, a Heineken "
            "subsidiary) started the Smallholder Alliance for Sorghum in Haiti "
            "(SMASH) program to build and reinforce a local sorghum supply chain. "
            "In support, they developed SMASH Mobil, an integrated mobile technology "
            "and reporting system, to mitigate the discrepancy between what was "
            "happening in the field and what was being reported, but also to "
            "support key monitoring and evaluation efforts. "
        ),
        ugettext_lazy(
            "The tool, supported by the CommCare platform, runs on Android tablets "
            "and helps the program monitor its progress in near real time, from land "
            "preparation and planting all the way to the delivery of grain to BRANA."
        ),
    ],
    partners=[
        "Brasserie Nationale d’Haïti",
        "the Inter-American Development Bank",
        "Papyrus S.A.",
    ],
    countries=[
        ugettext_lazy("Haiti"),
    ],
    sectors=[
        ugettext_lazy("Agricultural Logistics"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Decision & Diagnostic Support"),
        ugettext_lazy("Custom Reports"),
    ],
    slug="smash-mobil",
    primary_cta="feb466fe-fc2c-42e6-af29-b2dd64232f53",
    subnav_cta="512be50f-8b05-45ff-aa3c-7ad6e10299eb",
    event_tracking_title="SMASH Mobil",
)
