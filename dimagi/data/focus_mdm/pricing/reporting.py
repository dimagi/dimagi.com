from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Reporting and analytics"
    ),
    slug='reporting',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Show aggregated data on dashboard"
        ),
        description=ugettext_lazy(
            "Dashboard shows data aggregations (time usage, data usage, highest usage apps) "
            "and organization area coverage. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Standard Pre-built reports"
        ),
        description=ugettext_lazy(
            "Consists of Device Activity Report, Data Usage Report, "
            "Admin Activity Report "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Export report to excel file"
        ),
        description=ugettext_lazy(
            "Export report data to .xls file."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Scheduled reports"
        ),
        description=ugettext_lazy(
            "Send reports to a IT admin by email at a given time. "
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Custom"
        ),
        description=ugettext_lazy(
            "Create custom reports on demand. "
        ),
        support=Support(False, False, False, True),
    )
])
