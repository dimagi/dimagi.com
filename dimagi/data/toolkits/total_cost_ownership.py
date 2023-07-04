from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Total Cost of Ownership Model"
    ),
    tagline=ugettext_lazy(
        "Use the Total Cost of Ownership Model to budget for your "
        "mobile solution."
    ),
    image="total-cost-ownership",
    template="data/toolkits/summaries/total_cost_ownership.html",
    slug="total-cost-ownership",
    icon="svg/toolkits/icons/total_cost_ownership_model.html",
    theme="primary-theme",
    download_url="https://f.hubspotusercontent20.net/hubfs/503070/Toolkits/Dimagi-CommCare-TCO-Model-2018.xlsx",
    hubspot_form="19bbc2bc-d6a3-4831-8088-770393235a75",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        highlight_image="total-cost-ownership-highlights-one",
        description=ugettext_lazy("""
Map out the scale of your operation over time
to project how your growth will impact your
data collection costs.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        highlight_image="total-cost-ownership-highlights-two",
        description=ugettext_lazy("""
Consider whether your team will need
traning and how that might impact your
expenses.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        highlight_image="total-cost-ownership-highlights-three",
        description=ugettext_lazy("""
Know your monthly operating costs
such as your voice and data plan, as
well as your equipment.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.DIGITAL_HEALTH_STSTEMS,
    summary.DIGITAL_WORKFLOW_TEMPLATE,
])
