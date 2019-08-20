from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import OtherToolkit


BUSINESS_DEVELOPMENT = OtherToolkit(
    name=ugettext_lazy(
        "Business Development Toolkit"
    ),
    icon="svg/tookits/icons/business_development.html",
    description=ugettext_lazy("""
Use the Business Development Toolkit to develop a BD pipeline
for your organization.
    """),
    view_url="business-development",
)


COMMCARE_EVIDENCE_BASE = OtherToolkit(
    name=ugettext_lazy(
        "The CommCare Evidence Base"
    ),
    icon="svg/tookits/icons/commcare_evidence_base.html",
    description=ugettext_lazy("""
Over 60 studies have assessed CommCare's impact, making it the most
evidence-based mobile platform for frontline workers in low-resource
settings.
    """),
    view_url="commcare-evidence-base",
)


COMMCARE_MANAGING_DATA = OtherToolkit(
    name=ugettext_lazy(
        "Managing Data in CommCare"
    ),
    icon="svg/tookits/icons/managingdata_commcare.html",
    description=ugettext_lazy("""
A starter guide to inspecting, cleaning and exporting data in
CommCare.
    """),
    view_url="commcare-managing-data",
)


DATA_COLLECTION = OtherToolkit(
    name=ugettext_lazy(
        "Data Collection Guide"
    ),
    icon="svg/tookits/icons/data_collection.html",
    description=ugettext_lazy("""
Use this introductory guide to data collection to organize your data collection plan.
    """),
    view_url="data-collection",
)


MANAGING_DEVICES_EBOOK = OtherToolkit(
    name=ugettext_lazy(
        "Managing Devices at Scale"
    ),
    icon="svg/tookits/icons/managingdevices_scale.html",
    description=ugettext_lazy("""
Key learnings from managing thousands of devices in a
large-scale mobile health project.
    """),
    view_url="managing-devices-ebook",
)


MATURITY_MODEL = OtherToolkit(
    name=ugettext_lazy(
        "The Maturity Model"
    ),
    icon="svg/tookits/icons/maturity_model.html",
    description=ugettext_lazy("""
Use the Maturity Model to establish a long-term
vision for building and scaling your mobile system.
    """),
    view_url="maturity-model",
)


MOBILE_DATA_COLLECTION = OtherToolkit(
    name=ugettext_lazy(
        "Mobile Data Collection Guide"
    ),
    icon="svg/tookits/icons/mobile_data_collection.html",
    description=ugettext_lazy("""
Read this guide to learn almost everything you need to know to set up your own successful 
mobile data collection program.
    """),
    view_url="mobile-data-collection",
)


TOTAL_COST_OWNERSHIP = OtherToolkit(
    name=ugettext_lazy(
        "Total Cost of Ownership Model"
    ),
    icon="svg/tookits/icons/total_cost_ownership_model.html",
    description=ugettext_lazy("""
Use the Total Cost of Ownership Model to budget for your
mobile solution.
    """),
    view_url="total-cost-ownership",
)
