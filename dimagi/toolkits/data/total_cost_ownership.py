from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.toolkits.models import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Total Cost of Ownership Model"
    ),
    tagline=ugettext_lazy(
        "Use the Total Cost of Ownership Model to budget for your "
        "mobile solution."
    ),
    template="toolkits/summaries/total_cost_ownership.html",
    slug="total-cost-ownership",
    download_url="https://www.dropbox.com/s/ybtrlh3xtt2gqnn/Dimagi_-_CommCare_-_TCO_model_2017.xlsx?dl=1",
    hubspot_form="19bbc2bc-d6a3-4831-8088-770393235a75",
)
