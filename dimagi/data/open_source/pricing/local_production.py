from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.open_source import (
    SummaryGroup,
    Summary,
)


GROUP = SummaryGroup(
    title=ugettext_lazy(
        "Local Production Data Collection"
    ),
    slug='local-production',
)

GROUP.add_summary([
    Summary(
        title=ugettext_lazy(
            "Local Production Data Collection"
        ),
        description=ugettext_lazy(
            "Your local team stands up and maintains the CommCare production "
            "platform which is used for collecting and storing data. This "
            "involves system administration tasks such as regular CommCare "
            "code deploys, upgrading services, applying data security measures, "
            "and maintaining platform up-time. In certain geographies, we can "
            "recommend a local IT company with experience in server administration "
            "and maintenance of CommCare. A CommCare staging application is supported "
            "in the Dimagi-hosted SaaS environment and linked to the production local "
            "instance. This provides a staging environment for active app building and testing."
        ),
        specifics=ugettext_lazy(
            "Production data is submitted directly to the local instance and does not "
            "pass through the Dimagi-hosted instance."
        ),
        intensity=ugettext_lazy(
            "High"
        ),
        time=ugettext_lazy(
            "Variable"
        ),
        security=ugettext_lazy(
            "Variable"
        ),
        support=[
            ugettext_lazy("DevOps and infrastructure management (Dimagi-hosted environment only) "),
            ugettext_lazy("CommCare product support "),
            ugettext_lazy("Self-hosting Toolkit "),
            ugettext_lazy("CommCare developer forum "),
        ],
    ),
])
