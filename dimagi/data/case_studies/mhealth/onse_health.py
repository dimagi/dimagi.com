from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        " Enabling Supportive Supervision to Improve Health Outcomes in Malawi "
    ),
    summary=[
        ugettext_lazy(
            "The digital integrated supportive supervision (ISS) is a suite of digital "
            "supervision checklists that the Ministry of Health and Population (MoHP) in " 
            "Malawi is using to supervise health facilities and programs. The tool was "
            "developed by Dimagi in 2018, working as a technical partner on the USAID-supported "
            "Organized Network of Services for Everyone’s (ONSE) Health Activity. It is used by "
            "supervisors from district health management teams (DHMTs), and managers from zonal "
            "and national levels of the MoHP on a quarterly basis as a standard supervision, "
            "monitoring, oversight, and decision-making tool. "

            "Each of the 29 districts in Malawi are empowered with 5 tablets preloaded with "
            "the digital ISS app built on the CommCare platform. The integration with DHIS2 has "
            "eliminated duplication in data collection between DHIS2 and this national supervision "
            "tool built on CommCare. Having supported the transition to local ownership and technical "
            "capacity transfer in hosting and application building, Dimagi has ensured that the MoHP "
            "has the skills needed to adapt the ISS to meet emerging needs in the future and sustain "
            "it as a government owned and managed tool. "

        ),
    ],
    partners=[
       "Ministry of Health and Population (MoHP)",
       "Management Sciences for Health (MSH)",
       "USAID",
       "The Bill and Melinda Gates Foundation, Options Project",
    ],
    countries=[
        ugettext_lazy("Malawi"),
    ],
    sectors=[
        ugettext_lazy("Health Systems Strengthening /cross cutting all programs"),
    ],
    features=[
        ugettext_lazy("Case management"),
        ugettext_lazy("Decision Support"),
        ugettext_lazy("Action management"),
        ugettext_lazy("Visualizations"),
    ],
    slug="mhealth-onse",
    primary_cta="66fac504-3c3b-48eb-91ee-17d7a1bbe276",
    subnav_cta="4fcf9f51-d2d6-4729-b378-7c7ce8473a54",
    download_url_language="https://sites.dimagi.com/hubfs/Case Studies/Case Study - RTI.pdf",
    event_tracking_title="ONSE HEALTH",
)
