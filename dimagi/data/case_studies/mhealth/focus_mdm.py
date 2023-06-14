from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "SHM Foundation: FocusMDM for Improving Health, Education, and "
        "HIV Outcomes for Adolescents in South Africa"
    ),
    summary=[
        ugettext_lazy(
            "For more than a decade, SHM Foundation has sought to bring about "
            "positive social change by providing communities and individuals "
            "with practical tools and innovative solutions. They have extensive "
            "technical experience with mobile-based groups for those affected by HIV/AIDS."
        ),
        ugettext_lazy(
            "This project, starting in late 2019, creates mobile phone-based peer "
            "support groups to help HIV+ adolescents better understand and come to "
            "terms with their illness by linking them with trained peer mentors who "
            "have previously gone through similar groups as participants."
        ),
        ugettext_lazy(
            "SHM Foundation has partnered with Dimagi to implement FocusMDM "
            "as their preferred device management tool. The platform affords "
            "participants a degree of autonomy and to use their phones as they "
            "wish (provided they do not contravene the permitted use cases). Using "
            "data usage analytics and device rules built into FocusMDM, SHM "
            "Foundation administrators can limit or ban the use of mobile data "
            "for restricted or unwanted apps."
        ),
    ],
    partners=[
        "SHM Foundation",
    ],
    countries=[
        ugettext_lazy("South Africa"),
        ugettext_lazy("Zimbabwe"),
    ],
    sectors=[
        ugettext_lazy("Mental Health"),
    ],
    features=[
        ugettext_lazy("Device Usage Analytics"),
        ugettext_lazy("Device Rules"),
    ],
    slug="focus_mdm",
    primary_cta="acbd0ad3-4a98-4bbe-a8c4-1c075da2eefe",
    subnav_cta="e9908815-2b09-40eb-8a82-cc93250da337",
    event_tracking_title="SHM Foundation",
    theme = "orange-theme",
)
