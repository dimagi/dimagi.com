from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Mobile SAKHI Project: CommCare for Improving Maternal & Child Health"
    ),
    summary=[
        ugettext_lazy(
            "In 2013, Lata Medical Research Foundation (LMRF) partnered with "
            "Dimagi to assess CommCare’s feasibility for monitoring antenatal, "
            "natal, and post-natal care, as well as infant nutrition, in rural "
            "India. LMRF adopted CommCare to help accredited social health "
            "activists (ASHAs) track pregnant women and improve their "
            "health-seeking behavior and maternal & child health outcomes by "
            "familiarizing them and their families with available public "
            "health programs."
        ),
    ],
    partners=[
        "Lata Medical Research Foundation (LMRF)",
        "Government of India",
        "National Health and Medical Research Council (NHMRC) through "
        "the University of Sydney, & Nutrition Embedding Evaluation Program (NEEP) through PATH",
    ],
    countries=[
        ugettext_lazy("India"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
    ],
    features=[
    ],
    slug="mhealth-lmrf-india",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20Mobile%20SAKHI%20Case%20Study.pdf",
    hubspot_form="0480314e-ca07-4a8d-857c-15c3f94f86c7",
)
