from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.open_source import (
    SummaryGroup,
    Summary,
)


GROUP = SummaryGroup(
    title=ugettext_lazy(
        "Local Mirrored Data Storage "
    ),
    slug='data-storage',
)

GROUP.add_summary([
    Summary(
        title=ugettext_lazy(
            "Local Mirrored Data Storage"
        ),
        description=ugettext_lazy(
            "The CommCare platform is supported by the Dimagi-hosted SaaS "
            "environment. This service includes system administration tasks "
            "such as regular CommCare code deploys, upgrading services, applying "
            "data security measures, and maintaining platform up-time. Additionally, "
            "your local team stands up and hosts an SQL database that stores the data "
            "locally, and a data pipeline is established between the platform and the "
            "local database, using manual intervention or CommCare features, such as "
            "the Data Export Tool."
        ),
        specifics=ugettext_lazy(
            "Data will be collected in the Dimagi-hosted environment "
            "and copied to the local database."
        ),
        intensity=ugettext_lazy(
            "Low"
        ),
        time=ugettext_lazy(
            "Immediate"
        ),
        security=ugettext_lazy(
            "Variable"
        ),
        support=ugettext_lazy(
            "DevOps and infrastructure management (Dimagi-hosted environment only)"
            "CommCare product support"
            "CommCare developer forum"
        ),
    ),
])
