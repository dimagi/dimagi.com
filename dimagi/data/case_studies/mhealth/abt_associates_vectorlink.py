from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "MOTECH Suite for Continuum of Care Services in India"
    ),
    summary=[
        ugettext_lazy(
            "CARE India, Dimagi and Grameen Foundation deployed the MOTECH "
            "Suite to improve delivery of family health interventions and "
            "quality of health services in rural India. "
        ),
        ugettext_lazy(
            "The system, called the Continuum of Care Services (CCS), offers "
            "a comprehensive tool for mobile workers, providing coordinated "
            "care for one million people in Bihar, India. Its aim is to cover "
            "the 1000-day window of pregnancy through the child’s second year "
            "of age, to deliver ‘the right messages at the right time’ to "
            "pregnant women and newborn children within the community. "
        ),
    ],
    partners=[
        "Bill & Melinda Gates Foundation",
        "Government of Bihar",
        "CARE India",
        "BBC Media Action",
        "Grameen Foundation",
        "Dimagi"
    ],
    countries=[
        ugettext_lazy("India"),
    ],
    sectors=[
        ugettext_lazy("Maternal, Newborn & Child Health including Nutrition (MNCHN)"),
    ],
    features=[
        ugettext_lazy("Decision support"),
        ugettext_lazy("Client management"),
        ugettext_lazy("Data collection & sharing"),
        ugettext_lazy("Mobile reports"),
        ugettext_lazy("Home visit scheduler"),
        ugettext_lazy("Call center"),
        ugettext_lazy("Referral system"),
        ugettext_lazy("EDD & BMI calculators"),
        ugettext_lazy("Multimedia"),
        ugettext_lazy("Performance dashboards"),
    ],
    slug="abt-associates-vectorlink",
    primary_cta="693139c3-51b7-4c58-a666-a049ee806d98",
    subnav_cta="e51a99d3-fcd6-4065-b414-774c3523e4eb",
    event_tracking_title="Abt Associates VectorLink",
)
