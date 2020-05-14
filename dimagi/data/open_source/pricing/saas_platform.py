from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.open_source import (
    SummaryGroup,
    Summary,
)


GROUP = SummaryGroup(
    title=ugettext_lazy(
        "Dimagi-Hosted SaaS Platform "
    ),
    slug='sass-platform',
)

GROUP.add_summary([
    Summary(
        title=ugettext_lazy(
            "Dimagi-Hosted SaaS Platform "
        ),
        description=ugettext_lazy(
            "The CommCare platform is supported by the Dimagi-hosted "
            "SaaS environment. This service includes system administration "
            "tasks such as regular CommCare code deploys, upgrading services, "
            "applying data security measures, and maintaining platform up-time."
        ),
        specifics=ugettext_lazy(
            "Data collected and stored in Dimagi-hosted environment"
        ),
        intensity=ugettext_lazy(
            "Lowest"
        ),
        time=ugettext_lazy(
            "Immediate"
        ),
        security=ugettext_lazy(
            "HIPAA, GDPR, ISO, and SOC3 compliance"
        ),
        support=[
            ugettext_lazy("DevOps and infrastructure management"),
            ugettext_lazy("CommCare product support"),
            ugettext_lazy("CommCare developer forum"),
        ],
    ),
])
