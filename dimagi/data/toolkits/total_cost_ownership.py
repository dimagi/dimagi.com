from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Total Cost of Ownership Model"
    ),
    tagline=ugettext_lazy(
        "Use the Total Cost of Ownership Model to budget for your "
        "mobile solution."
    ),
    template="data/toolkits/summaries/total_cost_ownership.html",
    slug="total-cost-ownership",
    icon="svg/tookits/icons/Total Cost_Ownership_Model.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Dimagi-CommCare-TCO-Model-2018-2.xlsx",
    hubspot_form="19bbc2bc-d6a3-4831-8088-770393235a75",
)
