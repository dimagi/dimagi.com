from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "USAID Cambodia Integrated Early Childhood Development Activity"
    ),
    summary=[
        ugettext_lazy(
          "RTI International launched the Integrated Early Childhood Development (IECD) "
          "Activity in July 2020, funded by USAID/Cambodia. It supports vulnerable newborns"
          "and young children to reach their full developmental potential through nurturing "
          "care and intensive interventions during the first 1,000 days. "
        ),
        ugettext_lazy(   
          "The multi-sectoral approach delivers on the following: "
            "<ul class='unorderedlist'> <li> Strengthens nutrition delivery service at communities </li>"
            "<li> Supports nutrition-sensitive agriculture and improved livelihoods </li>"
            "<li> Improves water, sanitation, and hygiene practices among caregiver </li>"
            "<li> Promotes responsive caregiving to help children meet critical milestones </li>"
            "<li> Supports developmental milestone screening </li> </ul>"

        ),    
    ],
    partners=[
        "RTI International ",
    ],
    countries=[
        ugettext_lazy(" Cambodia "),
    ],
    sectors=[
        ugettext_lazy(" Early Childhood Development, Agriculture, Nutrition, Disability Inclusion"),
    ],
    features=[
        ugettext_lazy("Case management"),
        ugettext_lazy("Decision & Diagnostic Support"),
        ugettext_lazy(" Multimedia"),
        ugettext_lazy("Mobile Reports"),
    ],
    slug="mhealth-rti",
    primary_cta="66fac504-3c3b-48eb-91ee-17d7a1bbe276",
    subnav_cta="4fcf9f51-d2d6-4729-b378-7c7ce8473a54",
    download_url_language="https://sites.dimagi.com/hubfs/Case Studies/Case Study - RTI.pdf",
    event_tracking_title="RTI USAID",
    theme = "primary-theme",
)
