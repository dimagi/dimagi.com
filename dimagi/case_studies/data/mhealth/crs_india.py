from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Using mHealth to reduce maternal & newborn deaths in India"
    ),
    summary=ugettext_lazy(
        "In 2011, Catholic Relief Services (CRS) collaborated with the "
        "National Heath Mission (NHM) in Uttar Pradesh, India to establish "
        "the Reducing Maternal and Newborn Deaths (ReMiND) project to improve "
        "the delivery of community-level prenatal and postnatal care and "
        "support services. CRS worked with Dimagi to develop a customized, "
        "mobile health (mHealth) application for the government’s frontline "
        "health workers using Dimagi’s open source mobile platform, CommCare. "
        "Since its pilot deployment, the ReMiND project has successfully "
        "matured from an initial proof of concept to a scaled mobile tool "
        "for community health workers."
    ),
    partners=[
        "Catholic Relief Services",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("India"),
    ],
    sectors=[
        ugettext_lazy("Maternal, Neonatal, and Child Health (MNCH)"),
    ],
    features=[
        ugettext_lazy("Case management"),
        ugettext_lazy("Data Collection"),
        ugettext_lazy("Supervision apps"),
        ugettext_lazy("Referrals"),
        ugettext_lazy("Multimedia Counselling"),
        ugettext_lazy("SMS Reminders"),
    ],
    slug="mhealth-crs-india",
    download_url="https://www.dropbox.com/s/lg8fd0x2z7x7py5/mhealth-crs-india.pdf?dl=1",
    hubspot_form="d5f0286b-6605-4a22-a105-aedd2bbdd42e",
)
