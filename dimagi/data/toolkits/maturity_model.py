from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit
from dimagi.pages.models.toolkits import Toolkit, Highlight, OtherToolkit


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
    download_url="https://www.dropbox.com/s/juqabe8bykwuq3n/Dimagi%20Maturity%20Model.zip?dl=1",
    hubspot_form="edd74f83-1893-43a3-bb60-f31e20e5f43a",
    hubspot_formId="d8869004-bfed-4cfd-8e28-cf395b0b5b9a",
    icon="svg/case_management/broken_link.html",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
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
        description=ugettext_lazy("""
Set a long-term plan for your project and
how you will manage your mobile solution
in the coming years.
        """),
    ),  
])


TOOLKIT.add_other_toolkits([
    OtherToolkit(
        name=ugettext_lazy(
            "Business Development Toolkit"
        ),
        icon="svg/case_management/broken_link.html",
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
        icon="svg/case_management/broken_link.html",
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
        icon="svg/case_management/broken_link.html",
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
        icon="svg/case_management/broken_link.html",
        description=ugettext_lazy("""
Key learnings from managing thousands of devices in a
large-scale mobile health project.
        """),
        view_url="managing-devices-ebook",
    ),
    OtherToolkit(
        name=ugettext_lazy(
            "Total Cost of Ownership Model"
        ),
        icon="svg/case_management/broken_link.html",
        description=ugettext_lazy("""
Use the Total Cost of Ownership Model to budget for your
mobile solution.
        """),
        view_url="total-cost-ownership",
    ),  
])