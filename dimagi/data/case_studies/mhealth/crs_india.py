from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Catholic Relief Services: Reducing Maternal and Newborn Deaths (ReMiND)"
    ),
    summary=[
        ugettext_lazy(
            "In 2011, Catholic Relief Services (CRS) collaborated with the "
            "National Health Mission (NHM) in Uttar Pradesh, India to establish "
            "the Reducing Maternal and Newborn Deaths (ReMiND) project. Its goal "
            "was to improve the delivery of community-level prenatal and postnatal "
            "care and support services to local mothers and families. CRS worked "
            "with Dimagi to develop a customized, mobile health (mHealth) CommCare "
            "application for the government’s frontline health workers. Since its "
            "pilot deployment of 10 users, the ReMiND project has successfully "
            "matured from an initial proof of concept to a scaled mobile tool for "
            "community health workers covering a population of "
            "over 300,000."
        ),
    ],
    partners=[
        "Catholic Relief Services",
        "Department of Health and Family Welfare, Uttar Pradesh",
    ],
    countries=[
        ugettext_lazy("India"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Newborn Health"),
    ],
    features=[
        ugettext_lazy("Case management"),
        ugettext_lazy("Data Collection"),
        ugettext_lazy("Supervision apps"),
        ugettext_lazy("Referrals"),
        ugettext_lazy("Multimedia Counseling"),
        ugettext_lazy("SMS Reminders"),
    ],
    slug="mhealth-crs-india",
    primary_cta="37a68280-3d6c-4211-b1f8-1e98a8b93b6f",
    subnav_cta="c7531703-2b83-46eb-ace9-9646a3168967",
    event_tracking_title="Catholic Relief Services",
)
