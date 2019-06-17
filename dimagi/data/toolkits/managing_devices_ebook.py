from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit
from dimagi.pages.models.toolkits import Toolkit, Highlight, OtherToolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Managing Devices at Scale"
    ),
    tagline=ugettext_lazy(
        "Key learnings from managing thousands of devices in a "
        "large-scale mobile health project."
    ),
    image="managing-devices-ebook",
    template="data/toolkits/summaries/managing_devices_ebook.html",
    slug="managing-devices-ebook",
    icon="svg/tookits/icons/managingdevices_scale.html",
    download_url="https://www.dropbox.com/s/lk5gujyrk3lm7v7/Managing%20Devices%20at%20Scale.pdf?dl=1",
    hubspot_form="186d64b8-8dcc-45d3-af92-03259efc96a8",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        highlight_image="managing-devices-ebook-highlights-one",
        description=ugettext_lazy("""
Aligning responsibilities across
stakeholders is key while rolling out a
mobile project at scale.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        highlight_image="managing-devices-ebook-highlights-two",
        description=ugettext_lazy("""
Know what details you should
include in your explanation guide
for your device.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        highlight_image="managing-devices-ebook-highlights-three",
        description=ugettext_lazy("""
When should you set up a call center
or help desk for support? Our team
weighs in.
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