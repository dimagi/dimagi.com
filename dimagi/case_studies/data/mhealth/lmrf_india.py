from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Using mHealth to Improve Antenatal, Natal, & Post-Natal Care in India"
    ),
    summary=ugettext_lazy(
        "Lata Medical Research Foundation (LMRF) partnered with Dimagi "
        "to assess CommCare’s feasibility for monitoring antenatal, "
        "natal and postnatal care and infant nutrition in rural India. "
        "After an initial successful study, LMRF adopted CommCare in "
        "2013 to help frontline workers track pregnant women, and "
        "familiarize them, as well as their families, with public health "
        "programs to improve their health seeking behavior, and "
        "consequently, maternal and child health outcomes."
    ),
    partners=[
        "India Lata Medical Research Foundation",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("India"),
    ],
    sectors=[
        ugettext_lazy("Maternal health"),
        ugettext_lazy("Child health"),
        ugettext_lazy("Nutrition"),
    ],
    features=[
        ugettext_lazy("data collection"),
        ugettext_lazy("case management"),
        ugettext_lazy("multimedia & counseling"),
        ugettext_lazy("auto calculation of EDD, gestational age, "
                      "age of the infant, date of next scheduled visit"),
        ugettext_lazy("skip logic"),
        ugettext_lazy("data editing feature"),
    ],
    slug="mhealth-lmrf-india",
    download_url="https://www.dropbox.com/s/kc43w1s2yb2mau0/mhealth-lmrf-india.pdf?dl=1",
)
