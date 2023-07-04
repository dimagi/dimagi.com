from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Suaahara II: CommCare for Community-Based Maternal & Child Health"
    ),
    summary=[
        ugettext_lazy(
            "Suaahara II (SII) is a seven-year USAID-funded program using a household-based "
            "approach to improve the nutritional status of pregnant and lactating women and "
            "children under two years of age. Building on the learnings from Suaahara I (SI), "
            "Suaahara partners have implemented a combination of nutrition-specific and "
            "nutrition-sensitive interventions throughout 42 of Nepal’s 77 districts."
        ),
        ugettext_lazy(
            "The program’s goals are wide-ranging, include to improve the quality and use of "
            "maternal and child health and nutrition services; increase ideal household "
            "practices related to health, family planning, nutrition, and water, sanitation, "
            "and hygiene; ensure community access to and consumption of nutritious foods in "
            "areas with very poor nutrition indicators; and improve nutrition governance."
        ),
        ugettext_lazy(
            "All SII interventions are based on social and behavior change communication (SBCC) "
            "with a  focus on gender equity and social inclusion. Digital platforms for data "
            "collection, follow-up, and service delivery also support monitoring, evaluation, and "
            "research for learning (MERL) practices and continuous program improvement."
        ),
    ],
    partners=[
        "Helen Keller International (HKI)",
        "CARE",
        "FHI360",
        "Equal Access, Nepali Technical Assistance Group (NTAG)",
        "Environment and Public Health Organization (ENPHO)",
        "Vijaya Development Resource Centre (VDRC)",
    ],
    countries=[
        ugettext_lazy("Nepal"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
        ugettext_lazy("Nutrition"),
    ],
    features=[
        ugettext_lazy("Linked domains"),
        ugettext_lazy("DHIS2 integration"),
    ],
    slug="suaahara-II-mch",
    primary_cta="53c200e4-09a1-4733-a47a-2c9cb64cbdcc",
    subnav_cta="b33a5569-6d06-4720-b862-069b8d0d1ace",
    event_tracking_title="Suaahara II",
    theme = "orange-theme",
)
