from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.open_source import (
    SummaryGroup,
    Summary,
)


GROUP = SummaryGroup(
    title=ugettext_lazy(
        "Independent CommCare Self-Hosting"
    ),
    slug='self-hosting',
)

GROUP.add_summary([
    Summary(
        title=ugettext_lazy(
            "Independent CommCare Self-Hosting"
        ),
        description=ugettext_lazy(
            "Your local team stands up and maintains the CommCare production "
            "platform which is used for collecting and storing data. This "
            "involves system administration tasks such as regular CommCare "
            "code deploys, upgrading services, applying data security measures, "
            "and maintaining platform up-time. In certain geographies, we can "
            "recommend a local IT company with experience in server administration "
            "and maintenance of CommCare."
        ),
        specifics=ugettext_lazy(
            "Data is submitted directly to the local CommCare instance. There "
            "is no connection to any Dimagi-hosted environments."
        ),
        intensity=ugettext_lazy(
            "Highest"
        ),
        time=ugettext_lazy(
            "Variable"
        ),
        security=ugettext_lazy(
            "Variable"
        ),
        support=ugettext_lazy(
            "CommCare developer forum"
        ),
    ),
])
