from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Infomovel: CommCare for HIV and TB Patient Tracking"
    ),
    summary=[
        ugettext_lazy(
            "Infomovel is a patient tracking tool developed to support "
            "community health workers (CHWs) administer services across "
            "seven provinces in Mozambique. Focused on HIV/AIDS, tuberculosis, "
            "and prevention of mother-to-child transmission (PMTCT), the tool "
            "was originally piloted in 2015 with Ariel Glaser Foundation in "
            "Cabo Delgado. In 2019, the program expanded to national scale, "
            "supporting more than 1,750 workers across eight different "
            "implementing partners."
        ),
        ugettext_lazy(
            "Infomovel supports linkages between community workers and health "
            "facility focal points by including case management support for HIV "
            "testing and counseling (HTC), care & treatment (C&T), PMTCT, and "
            "tuberculosis programmatic workflows. Infomovel consists of two "
            "applications, Health Facility and Community, which support patient "
            "registration, follow-up, defaulter tracking, and household testing. "
        ),
    ],
    partners=[
        "Center for Disease Control",
        "Friends in Global Health",
        "Fundação Ariel Glaser",
        "Elizabeth Glaser Pediatrics Aids Foundation",
        "Centro de Colaboração em Saude",
        "ICAP",
        "Mothers2Mothers",
        "N’weti",
    ],
    countries=[
        ugettext_lazy("Mozambique"),
    ],
    sectors=[
        ugettext_lazy("HIV/AIDS and TB"),
    ],
    features=[
        ugettext_lazy("Client Case Management"),
        ugettext_lazy("EMR & OpenMRS Integration"),
        ugettext_lazy("Import Validation"),
        ugettext_lazy("Case Sharing"),
        ugettext_lazy("Multimedia-based Counseling"),
        ugettext_lazy("In-app Adherence Calculators"),
    ],
    slug="infomovel",
    download_url="https://f.hubspotusercontent20.net/hubfs/503070/Case%20Studies/CommCare%20-%20Infomovel%20Case%20Study.pdf",
    hubspot_form="53e6bbdf-5ce2-4a1f-b9e2-d7741c43a94a",
)
