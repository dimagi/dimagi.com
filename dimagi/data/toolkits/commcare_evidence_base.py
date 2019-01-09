from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.toolkits import Toolkit
from dimagi.pages.models.toolkits import Toolkit, Highlight, OtherToolkit


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "The CommCare Evidence Base"
    ),
    tagline=ugettext_lazy(
        "Over 50 studies have assessed CommCare's impact, making it the most "
        "evidence-based mobile platform for frontline workers in low-resource "
        "settings."
    ),
    image="commcare-evidence-base",
    template="data/toolkits/summaries/commcare_evidence_base.html",
    slug="commcare-evidence-base",
    icon="svg/tookits/icons/commcare_evidence_base.html",
    download_url="https://www.dropbox.com/s/chn7t7dsubhe9qb/CommCare-Evidence-Base-July-2016.pdf?dl=1",
    hubspot_form="f9b416b1-eb8b-430b-a2b6-644481b64a69",
    hubspot_formId="60812c12-0865-4c3d-b1e1-64e6570071d9",
)


TOOLKIT.add_highlights([
    Highlight(
        name=ugettext_lazy(
            "The CommCare Evidence Base"
        ),
        description=ugettext_lazy("""
An RCT in South Africa found that
FLWs using CommCare for
cardiovascular disease (CVD) screenings
took 75% less time...
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Data in CommCare"
        ),
        description=ugettext_lazy("""
In a study with Pathfinder
international, the use of CommCare
helped increase the provisionof HIV
tests from 67.5% to 82.2%.
        """),
    ),
    Highlight(
        name=ugettext_lazy(
            "Managing Devices at Scale"
        ),
        description=ugettext_lazy("""
After incorprating performance feedback,
frontline workers in one study made
21.5% more visits than control group over
a 12-month period.
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
            "The Maturity Model"
        ),
        icon="svg/case_management/broken_link.html",
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
        icon="svg/case_management/broken_link.html",
        description=ugettext_lazy("""
Use the Total Cost of Ownership Model to budget for your
mobile solution.
        """),
        view_url="total-cost-ownership",
    ),  
])