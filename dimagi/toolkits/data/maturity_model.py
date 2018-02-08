from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.toolkits.models import Toolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The Maturity Model"
    ),
    tagline=ugettext_lazy(
        "Use the Maturity Model to establish a long-term "
        "vision for building and scaling your mobile system"
    ),
    template="toolkits/summaries/maturity_model.html",
    slug="maturity-model",
    download_url="https://www.dropbox.com/s/juqabe8bykwuq3n/Dimagi%20Maturity%20Model.zip?dl=1",
)
