from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The Maturity Model"
    ),
    tagline=ugettext_lazy(
        "Use the Maturity Model to establish a long-term "
        "vision for building and scaling your mobile system."
    ),
    image="maturity-model",
    template="data/toolkits/summaries/maturity_model.html",
    slug="maturity-model",
    icon="svg/tookits/icons/maturity_model.html",
    download_url="https://f.hubspotusercontent20.net/hubfs/503070/Toolkits/Dimagi%20Maturity%20Model.zip",
    hubspot_form="edd74f83-1893-43a3-bb60-f31e20e5f43a",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        highlight_image="maturity-model-highlights-one",
        description=ugettext_lazy("""
Take a 30-minute assessment to see
what stage of maturity your project is
at across six program areas.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        highlight_image="maturity-model-highlights-two",
        description=ugettext_lazy("""
Identify opportunities for growth so
that you can manage your time and
palnning accordingly.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        highlight_image="maturity-model-highlights-three",
        description=ugettext_lazy("""
Set a long-term plan for your project and
how you will manage your mobile solution
in the coming years.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.BUSINESS_DEVELOPMENT,
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
])
