from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        " Enabling Supportive Supervision to Improve Health Outcomes in Malawi "
    ),
    summary=[
        ugettext_lazy(
            "The Ministry of Health and Population in Malawi (MoHP) uses the digital integrated supportive "
            "supervision (ISS) developed by Dimagi to supervise health facilities and programs. The tool is" 
            "standard for supervision, monitoring, and decision-making used by district health management "
            "teams (DHMTs) and MoHP managers. Dimagi has supported the transition to local ownership and "
            "technical capacity transfer for sustainability."

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
        ugettext_lazy("Health Systems Strengthening"),
    ],
    features=[
        ugettext_lazy("Case management"),
        ugettext_lazy("Decision Support"),
        ugettext_lazy("Action Management"),
        ugettext_lazy("Visualizations"),
    ],
    slug="mhealth-onse",
    primary_cta="c14fb752-2564-4f52-b37e-35e05ba0c735",
    subnav_cta="52b2fc91-77f6-4f41-a098-a2496ca59531",
    download_url_language="https://sites.dimagi.com/hubfs/Case Studies/Case Study - ONSE Malawi CS.pdf",
    event_tracking_title="ONSE HEALTH",
    theme = "primary-theme",
)
