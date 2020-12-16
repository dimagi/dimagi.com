from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "EGPAF & Baylor University: CommCare for HIV Patient Tracking and Appointment Reminders"
    ),
    summary=[
        ugettext_lazy(
            "Elizabeth Glaser Pediatric AIDS Foundation (EGPAF) and Dimagi "
            "collaborated in Lesotho to develop a CommCare patient tracking "
            "mobile solution to track patients' clinic appointments, send "
            "automated SMS reminders of clinic appointment date, facilitate "
            "patient tracking, and report on chosen outcomes as part of a "
            "comprehensive HIV, TB prevention, and maternal and child "
            "healthcare (MCH) and treatment program. The overall aim of the "
            "project, which was later supported in two additional districts "
            "by a team at Baylor College of Medicine Children’s Foundation, was "
            "to reduce missed appointments and the number of patients that are "
            "Lost to Follow Up (LTFU), especially those in the target population "
            "of pregnant women who are receiving ART (Antiretroviral Therapy)."
        ),
        ugettext_lazy(
            "The program aimed to reduce the number of patients in HIV, TB, and "
            "MCH programs missing their health facility appointments by sending "
            "personalized, confidential SMS appointment reminder messages to "
            "patients, and reducing the time and effort for health facility "
            "and client tracking workers to follow-up on patients, providing "
            "cleaner, more efficient ways of following up on those patients "
            "who miss appointments."
        ),
    ],
    partners=[
        "EGPAF-Lesotho",
        "Baylor College of Medicine Children’s Foundation Lesotho - ETHICS",
        "Lesotho Network of AIDs Services Organizations (LENASO)",
        "MOH"
    ],
    countries=[
        ugettext_lazy("Lesotho"),
    ],
    sectors=[
        ugettext_lazy("HIV/AIDS"),
    ],
    features=[
        ugettext_lazy("Case management"),
        ugettext_lazy("SMS Reminders"),
        ugettext_lazy("GPS"),
    ],
    slug="egpaf-baylor-hiv-tracking",
    primary_cta="208f8f02-4458-4366-a5f0-3c57e3d25a81",
    subnav_cta="50fb7304-02e3-4be5-82b6-6961d758b409",
    event_tracking_title="EGPAF HIV Tracking",
)
