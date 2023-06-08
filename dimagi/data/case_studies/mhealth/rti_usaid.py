from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "USAID Cambodia Integrated Early Childhood Development Activity"
    ),
    summary=[
        ugettext_lazy(
          "RTI International launched the USAID/Cambodia-funded "
          "Integrated Early Childhood Development (IECD) Activity "
          "in July 2020 to support children to thrive and reach their full "
          "developmental potential. The IECD Activity aims to promote "
          "nurturing care for the most vulnerable newborns and young children, "
          "starting before birth. Focus is on the early childhood years, with an "
          "emphasis on the first 1,000 days, for more intensive nutritional, "
          "psychosocial, and physical stimulation interventions.The IECD Activity "
          "supports child development holistically, through a multi-sectoral approach "
          "that includes the following: "

            "Strengthens nutrition delivery service at communities "
            "Supports nutrition-sensitive agriculture and improved livelihoods "
            "Improves water, sanitation, and hygiene practices among caregiver "
            "Promotes responsive caregiving to help children meet critical cognitive, linguistic, socio-emotional, and physical developmental milestones. "
            "Supports developmental milestone screening to enable the early identification of and interventions "
            "for children with developmental delays or who are at risk for impairments and disabilities. "
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
    primary_cta="37a68280-3d6c-4211-b1f8-1e98a8b93b6f",
    subnav_cta="c7531703-2b83-46eb-ace9-9646a3168967",
    event_tracking_title="RTI USAID",
)
