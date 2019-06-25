from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit
from dimagi.pages.models.toolkits import Toolkit, Highlight, OtherToolkit


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
    icon="svg/tookits/icons/total_cost_ownership_model.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Dimagi-CommCare-TCO-Model-2018-2.xlsx",
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
    OtherToolkit(
        name=ugettext_lazy(
            "Business Development Toolkit"
        ),
        icon="svg/tookits/icons/business_development.html",
        description=ugettext_lazy("""
Use the Business Development Toolkit to develop a BD pipeline
for your organization.
        """),
        view_url="business-development",
    ),
    OtherToolkit(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        icon="svg/tookits/icons/commcare_evidence_base.html",
        description=ugettext_lazy("""
Over 50 studies have assessed CommCare's impact, making it the most
evidence-based mobile platform for frontline workers in low-resource
settings.
        """),
        view_url="commcare-evidence-base",
    ),
    OtherToolkit(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        icon="svg/tookits/icons/managingdata_commcare.html",
        description=ugettext_lazy("""
A starter guide to inspecting, cleaning and exporting data in
CommCare.
        """),
        view_url="commcare-managing-data",
    ),
    OtherToolkit(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        icon="svg/tookits/icons/managingdevices_scale.html",
        description=ugettext_lazy("""
Key learnings from managing thousands of devices in a
large-scale mobile health project.
        """),
        view_url="managing-devices-ebook",
    ),
    OtherToolkit(
        name=ugettext_lazy(
            "The Maturity Model"
        ),
        icon="svg/tookits/icons/maturity_model.html",
        description=ugettext_lazy("""
Use the Maturity Model to establish a long-term
vision for building and scaling your mobile system.
        """),
        view_url="maturity-model",
    ), 
    OtherToolkit(
        name=ugettext_lazy(
            "Digital Health Interventions Checklist"
        ),
        icon="svg/tookits/icons/digital_health_interventions.html",
        description=ugettext_lazy("""
Learn how to describe your digital health technology across stakeholders .
        """),
        view_url="digital-health-interventions",
    ), 
    OtherToolkit(
        name=ugettext_lazy(
            "Mobile Data Collection Guide"
        ),
        icon="svg/tookits/icons/mobile_data_collection.html",
        description=ugettext_lazy("""
Read this guide to learn almost everything you need to know to set up your own successful 
mobile data collection program.
        """),
        view_url="mobile-data-collection",
    ),     
])