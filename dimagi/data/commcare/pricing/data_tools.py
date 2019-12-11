from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Data Tools"
    ),
    slug='data-tools',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Data exports"
        ),
        description=ugettext_lazy(
            "Export your CommCare data—including form submissions and "
            "case data—for use in 3rd party tools. Leverage built-in tools "
            "to customize your exports by date, user group, and more."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Data exploration"
        ),
        description=ugettext_lazy(
            "View data submitted by your field staff with built-in "
            "reports showing case information and form submissions, "
            "complete with current and historical values."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Pre-built project performance reports"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Scheduled email reports"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Excel dashboards"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Case importer"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Report builder"
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Data cleaning"
        ),
        description=ugettext_lazy(
            "Ensure your CommCare data is clean and accurate using data "
            "cleaning features to edit erroneous or incorrect form "
            "submissions and archive test data."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Power BI and Tableau integration"
        ),
        description=ugettext_lazy(
            "Send your CommCare data directly to Microsoft Power BI or "
            "Tableau for beautiful reporting and deep analytics. CommCare's "
            "integration employs OData feeds, enabling you to automatically "
            "refresh your data directly from Power BI and Tableau."
        ),
        support=Support(False, "Add On", True, False),
    ),
])
