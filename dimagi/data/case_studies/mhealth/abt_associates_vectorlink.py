from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Abt Associates – VectorLink: CommCare for Reducing Malaria"
    ),
    summary=[
        ugettext_lazy(
            "The Malaria Initiative Africa Indoor Residual Spraying (PMI AIRS) "
            "program is dedicated to reducing malaria in Africa through an "
            "innovative, community-driven approach that includes Indoor Residual "
            "Spraying (IRS). IRS involves spraying insecticide on the walls, "
            "ceilings, and other common indoor resting places of mosquitoes."
        ),
        ugettext_lazy(
            "In 2014, Dimagi joined the US President Malaria Initiative (PMI) and "
            "Abt Associates to provide an mHealth solution for sustainable intervention. "
            "The tools and systems provide efficient access to daily spray activity "
            "indicators and improve supervisory efforts. The project has resulted in "
            "preventing millions from contracting malaria throughout the African continent."
        ),
    ],
    partners=[
        "Abt Associates",
        "PMI VectorLink",
    ],
    countries=[
        ugettext_lazy("Benin"),
        ugettext_lazy("Burkina Faso"),
        ugettext_lazy("Côte d’Ivoire"),
        ugettext_lazy("Ethiopia"),
        ugettext_lazy("Ghana"),
        ugettext_lazy("Kenya"),
        ugettext_lazy("Madagascar"),
        ugettext_lazy("Malawi"),
        ugettext_lazy("Mali"),
        ugettext_lazy("Mozambique"),
        ugettext_lazy("Rwanda"),
        ugettext_lazy("Senegal"),
        ugettext_lazy("Sierra Leone"),
        ugettext_lazy("Tanzania"),
        ugettext_lazy("Uganda"),
        ugettext_lazy("Zambia"),
        ugettext_lazy("Zimbabwe"), 
    ],
    sectors=[
        ugettext_lazy("Infectious Disease"),
        ugettext_lazy("Maternal & Child Health"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Custom Reporting"),
        ugettext_lazy("Two-way SMS Functionality"),
        ugettext_lazy("Conditional Alerts"),
        ugettext_lazy("Submission of Form via SMS"),
    ],
    slug="abt-associates-vectorlink",
    primary_cta="693139c3-51b7-4c58-a666-a049ee806d98",
    subnav_cta="e51a99d3-fcd6-4065-b414-774c3523e4eb",
    event_tracking_title="Abt Associates VectorLink",
    theme = "orange-theme",
)
