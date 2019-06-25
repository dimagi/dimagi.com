from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit, Highlight, OtherToolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Mobile Data Collection Guide"
    ),
    tagline=ugettext_lazy(
        "Learn how to set up a mobile data collection program."
    ),
    image="mobile-data-collection",
    template="data/toolkits/summaries/mobile_data_collection.html",
    slug="mobile-data-collection",
    icon="svg/tookits/icons/mobile_data_collection.html",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Pillar%20Page%20PDFs/Guide%20to%20Mobile%20Data%20Collection.pdf",
    hubspot_form="a6b961bf-2a93-4d93-b2b5-46f71f82fd72",
)

TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
Learn how your data requirements and the environmental implications of your 
program inform your choice of mobile platform.
        """),
        highlight_image="mobile-data-collection-highlight-one",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
Identify your user stories, design the structure of your system, and develop your 
content and delivery design.
        """),
        highlight_image="mobile-data-collection-highlight-two",
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
Discover all the different tests to put your application through – from quality assurance, 
usability testing, and pilot programs.
        """),
        highlight_image="mobile-data-collection-highlight-three",
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
            "Digital Health Interventions Checklist"
        ),
        icon="svg/tookits/icons/digital_health_interventions.html",
        description=ugettext_lazy("""
Learn how to describe your digital health technology across stakeholders .
        """),
        view_url="digital-health-interventions",
    ),    
])