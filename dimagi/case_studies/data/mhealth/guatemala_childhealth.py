from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Improving Rural Health in Guatemala with CommCare"
    ),
    summary=ugettext_lazy(
        "Alta Verapaz is a rural region of Guatemala with one of the "
        "highest burdens of maternal mortality in the world. With an "
        "indigenous population of nearly 1 million people, 78% of Alta "
        "Verapaz lives below the poverty line and has a severe lack of "
        "formal health services. To improve maternal care in Alta Verapaz, "
        "as well as address extremely high rates of malnutrition and "
        "malaria, TulaSalud adopted CommCare in 2012 to enhance their "
        "community mobile health (mHealth) program."
    ),
    partners=[
        "TulaSalud",
    ],
    countries=[
        ugettext_lazy("Guatemala"),
    ],
    sectors=[
        ugettext_lazy("Maternal health"),
        ugettext_lazy("malaria"),
        ugettext_lazy("malnutrition"),
    ],
    features=[
        ugettext_lazy("Patient registration & tracking"),
        ugettext_lazy("decision & diagnostic support"),
        ugettext_lazy("WHO Z scores"),
        ugettext_lazy("clinical workflow"),
        ugettext_lazy("custom reporting"),
        ugettext_lazy("transportation coordination"),
        ugettext_lazy("referral followup"),
    ],
    slug="mhealth-guatemala-childhealth",
    download_url="https://www.dropbox.com/s/gehewi5z55xkaw3/mhealth-guatemala-childhealth.pdf?dl=1",
)
