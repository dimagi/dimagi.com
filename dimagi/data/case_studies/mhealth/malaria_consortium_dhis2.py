from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Malaria Consortium’s upSCALE Program: Integrating CommCare with DHIS2 for Improved Reporting"
    ),
    summary=[
        ugettext_lazy(
            "Community health workers in Mozambique, known as agentes polivalentes "
            "elementares (APEs), are elected members of remote communities who are "
            "trained to provide basic healthcare. They conduct health-promotion activities "
            "and provide integrated community case management (iCCM) for malaria, pneumonia, "
            "and diarrhea for children aged 2-59 months. In 2016, Malaria Consortium and "
            "Dimagi built an application called upSCALE to support the APEs delivering their "
            "work, collecting and aggregating data from the different programme activities. "
            "When the Mozambican Ministry of Health selected a DHIS2 platform to collect "
            "community-level data sets and aggregate them into a set of national health "
            "indicators, Dimagi and Malaria Consortium adapted the upSCALE application "
            "with a complete integration with the new platform."
        ),
        ugettext_lazy(
            "CommCare’s interoperability with DHIS2 opens up the possibility of Dimagi’s "
            "systems to take advantage of the widely deployed reporting system that is "
            "currently used in more than 40 countries, including on a national level in "
            "countries such as Kenya, Tanzania, Uganda, Rwanda, Ghana, Liberia, Bangladesh, "
            "and Mozambique."
        ),
    ],
    partners=[
        "Malaria Consortium",
    ],
    countries=[
        ugettext_lazy("Mozambique"),
    ],
    sectors=[
        ugettext_lazy("Health"),
    ],
    features=[
        ugettext_lazy("CommCare + DHIS2 Integration"),
    ],
    slug="malaria-consortium-dhis2",
    primary_cta="b510f80b-492b-4691-a072-4ddd8b35d9f4",
    subnav_cta="dd431fbf-a6fa-4410-a62e-f28e8965a2e5",
    event_tracking_title="Catholic Relief Services",
)
