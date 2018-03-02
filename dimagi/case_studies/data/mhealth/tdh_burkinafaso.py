from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "An Integrated eDiagnostic Approach in 400 Clinics in Burkina Faso"
    ),
    summary=ugettext_lazy(
        "Terre des hommes (Tdh, www.tdh.ch) partnered with Dimagi to create "
        "a tablet-based application known as the Electronic Register of "
        "Consultations (REC). Built on Dimagi’s CommCare platform, the REC "
        "aims to increase nurses’ adherence to IMCI protocols by providing "
        "enhanced decision support and case management capacity. At the "
        "completion of the project, it is expected that the REC will used in "
        "25% of health clinics in Burkina Faso, reaching a total of "
        "600,000 children."
    ),
    partners=[
        "Terre des Hommes",
    ],
    countries=[
        ugettext_lazy("Burkina Faso"),
    ],
    sectors=[
        ugettext_lazy("Child health"),
        ugettext_lazy("Clinical Care"),
    ],
    features=[
        ugettext_lazy("case management"),
        ugettext_lazy("decision & diagnostic support"),
        ugettext_lazy("fully HIPAA compliant data collection"),
        ugettext_lazy("fully HIPAA compliant data collection"),
        ugettext_lazy("various growth charts"),
        ugettext_lazy("clinical workflows"),
        ugettext_lazy("data validation"),
        ugettext_lazy("multimedia"),

    ],
    slug="mhealth-tdh-burkinafaso",
    download_url="https://www.dropbox.com/s/oakh337uexf4zgj/mhealth-tdh-burkinafaso.pdf?dl=1",
    hubspot_form="0cb7b31e-d335-437d-80a8-61f3bea7600b",
)
