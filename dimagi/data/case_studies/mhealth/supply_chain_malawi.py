from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Adopting SMS to Improve Essential Medicines Stock in Malawi"
    ),
    summary=ugettext_lazy(
        "In Malawi, community health workers, also known as Health "
        "Surveillance Assistants (HSAs), provide Community Case "
        "Management (CCM). These HSAs carry and prescribe a defined "
        "list of essential medicines such as ORS, anti-malarials, "
        "antibiotics, and family planning commodities. The Improving "
        "Supply Chains for Community Case Management of Pneumonia and "
        "Other Common Diseases of Childhood project (SC4CCM), implemented "
        "by the JSI Research & Training Institute, Inc. (JSI R&T) funded "
        "by the Bill & Melinda Gates Foundation, has worked with the "
        "Malawi Ministry of Health in developing approaches to address "
        "the lack of data visibility in the health supply chain for "
        "HSAs, which contributes to poor product availability in hard "
        "to reach areas."
    ),
    partners=[
        "John Snow International",
        "USAID | DELIVER Project",
        "Malawi Ministry of Health",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("Malawi"),
    ],
    sectors=[
        ugettext_lazy("Supply Chain Management"),
    ],
    features=[],
    slug="mhealth-supply-chain-malawi",
    download_url="https://www.dropbox.com/s/s67h8pbnogbo1vq/mhealth-supply-chain-malawi.pdf?dl=1",
    hubspot_form="6c75de96-f702-43f4-9a54-ba7667a4af30",
)
