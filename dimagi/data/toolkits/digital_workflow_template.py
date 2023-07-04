from __future__ import absolute_import
from django.utils.translation import ugettext_lazy

from dimagi.data.toolkits import summary
from dimagi.pages.models.toolkits import Toolkit, Highlight


TOOLKIT = Toolkit(
    title=ugettext_lazy(
        "Digital Workflow Template"
    ),
    tagline=ugettext_lazy(
        "This guide presents examples and templates "
        "to create digital workflow documentation."
    ),
    image="diig-digital-workflow-template",
    template="data/toolkits/summaries/digital_workflow_template.html",
    slug="diig-digital-workflow-template",
    icon="svg/toolkits/icons/digital_workflow_toolkit.html",
    theme="primary-theme",
    primary_cta="efcab94f-e5b8-4452-b65f-6e2a726fcb6e",
    download_slides="c91aafa4-2489-44da-a89a-4313b5ccb1e2",
    subnav_cta="611518c2-9635-43fc-a097-ea6cfc285e41",
    download_slides_cta="1c111606-85b8-45b2-86aa-f43a05e4806f",
    event_tracking_title="DIIG Workflow Template - Google Slides",
)

TOOLKIT.add_highlights([
    Highlight(
        description=ugettext_lazy("""
Use workflow legends to understand workflow standards.
        """),
        highlight_image="diig-digital-workflow-template-highlights-one",
    ),
    Highlight(
        description=ugettext_lazy("""
View example “Current” and “Future State” workflows.
        """),
        highlight_image="diig-digital-workflow-template-highlights-two",
    ),
    Highlight(
        description=ugettext_lazy("""
Copy and paste template workflows to create your own workflows in easily editable tools.
        """),
        highlight_image="diig-digital-workflow-template-highlights-three",
    ),  
])


TOOLKIT.add_other_toolkits([
    summary.COMMCARE_EVIDENCE_BASE,
    summary.COMMCARE_MANAGING_DATA,
    summary.MANAGING_DEVICES_EBOOK,
    summary.DATA_COLLECTION,
    summary.MOBILE_DATA_COLLECTION,
    summary.TOTAL_COST_OWNERSHIP,
    summary.DIGITAL_HEALTH_STSTEMS,
])
