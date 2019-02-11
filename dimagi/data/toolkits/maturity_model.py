from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The Maturity Model"
    ),
    tagline=ugettext_lazy(
        "Use the Maturity Model to establish a long-term "
        "vision for building and scaling your mobile system."
    ),
    template="data/toolkits/summaries/maturity_model.html",
    slug="maturity-model",
    icon="svg/tookits/icons/maturity_model.html",
    download_url="https://www.dropbox.com/s/juqabe8bykwuq3n/Dimagi%20Maturity%20Model.zip?dl=1",
    hubspot_form="edd74f83-1893-43a3-bb60-f31e20e5f43a",
)
