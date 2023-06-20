from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Deploying MOTECH Suite for MNCH & Nutrition programs in 10+ countries"
    ),
    summary=[
        ugettext_lazy(
            "In an effort to supplement their global health and nutrition "
            "programs with mobile technology, World Vision has partnered "
            "with Dimagi and Grameen Foundation to deploy MOTECH Suite. "
            "To date, World Vision has adapted and contextualized five "
            "standardized mobile health (mHealth) applications in ten countries "
            "in Africa, India, South and Southeast Asia, with plans to start "
            "deployment to six more in 2014. "
        ),
        ugettext_lazy(
            "These programs utilize the applications for maternal, neonatal, "
            "and child health and nutrition, which are designed to support "
            "Frontline Health Workers (FHWs) to deliver these services mo   re efficiently. "
        ),
        ugettext_lazy(
            "The solution serves as a job aid and monitoring tool, and includes "
            "components to reinforce intervention protocols. The applications "
            "leverage standardized content and collaborative design, enabling "
            "support for FHWs and potential for stronger service delivery at "
            "a global scale."
        ),
    ],
    partners=[
        "World Vision",
        "Grameen Foundation",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("Burundi"),
        ugettext_lazy("India"),
        ugettext_lazy("Indonesia"),
        ugettext_lazy("Niger"),
        ugettext_lazy("Sierra Leone"),
        ugettext_lazy("Sri Lanka"),
        ugettext_lazy("Uganda"),
        ugettext_lazy("Zambia"),
    ],
    sectors=[
        ugettext_lazy("Maternal, Neonatal, and Child Health (MNCH)"),
        ugettext_lazy("Nutrition"),
    ],
    features=[
        ugettext_lazy("Global application templates & content"),
        ugettext_lazy("Z-score calculations for Weight-for-Age"),
        ugettext_lazy("Weight-for-Height, Height-forAge, MUAC"),
        ugettext_lazy("Growth charts"),
        ugettext_lazy("Advanced referral system"),
        ugettext_lazy("Excel dashboard & custom reports"),
        ugettext_lazy("SMS reminders"),
    ],
    slug="mhealth-world-vision-motech",
    primary_cta="78528acc-455a-4c2c-8f98-75f77cac06ec",
    subnav_cta="bc6549c1-3069-4093-8e92-06e9b711df01",
    event_tracking_title="World Vision MOTECH",
    theme = "orange-theme",
)
