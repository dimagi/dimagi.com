from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit, Highlight, OtherToolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Digital Health Interventions Checklist"
    ),
    tagline=ugettext_lazy(
        "Learn how to describe your digital health technology across stakeholders "
    ),
    image="digital-health-interventions",
    template="data/toolkits/summaries/digital_health_interventions.html",
    slug="digital-health-interventions",
    icon="svg/tookits/icons/digital_health_interventions.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/ALL_Digital%20Health%20Interventions%20Checklist_v2.pdf",
    hubspot_form="0e1517c2-5a8f-4dca-a442-11252bb305d8",
)

TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
Defines the shared language to describe the 
uses of digital technology for health.
        """),
        highlight_image="digital-health-interventions-highlight-one",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
Shares different sets of recommendations for 
clients, healthcare providers, health system 
managers, and data services.
        """),
        highlight_image="digital-health-interventions-highlight-two",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
Covers recommendations for specific 
initiatives from client health records 
management to health facilities assessment 
and targeted client communications.
        """),
        highlight_image="digital-health-interventions-highlight-three",
    ),  
])


TOOLKIT.add_other_toolkits([
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
            "Total Cost of Ownership Model"
        ),
        icon="svg/tookits/icons/total_cost_ownership_model.html",
        description=ugettext_lazy("""
Use the Total Cost of Ownership Model to budget for your
mobile solution.
        """),
        view_url="total-cost-ownership",
    ),
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
            "Data Collection Guide"
        ),
        icon="svg/tookits/icons/data_collection.html",
        description=ugettext_lazy("""
Use this introductory guide to data collection to organize your data collection plan.
        """),
        view_url="data-collection",
    ),      
])