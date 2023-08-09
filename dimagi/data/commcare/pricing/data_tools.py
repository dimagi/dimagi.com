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
        description=ugettext_lazy(
            "View pre-built reports to get a high-level overview of key "
            "indicators and drill down into your data."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Scheduled email reports"
        ),
        description=ugettext_lazy(
            "Schedule regular emails of key reports to specific email "
            "addresses."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Excel dashboards"
        ),
        description=ugettext_lazy(
            "Set up a real-time link between a form or case export on HQ and "
            "a preconfigured Excel report. Excel calculations and graphs will "
            "update automatically on a regular basis as new data comes in."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Case importer"
        ),
        description=ugettext_lazy(
            "Create or update cases in bulk using Excel. With this feature, "
            "you can make changes or create new cases quickly and effectively. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
    title=ugettext_lazy(
            "Case List Explorer (CLE)"
        ),
        description=ugettext_lazy(
            "Case List Explorer is a powerful feature for CommCare HQ which enables users "
            "to inspect their case data by building custom-filtered views of their cases. "
            "The Case List Explorer allows you to find and validate test data, identify "
            "cases that fit a very specific criteria, and find data anomalies and outlies."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Report builder"
        ),
        description=ugettext_lazy(
            "Create custom reports from data collected in your CommCare "
            "applications, and schedule automated emails to share those "
            "custom reports on a recurring schedule. Subscription plans "
            "with Report Builder include up to 5 saved reports. "
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
        support=Support(False, "Add On", True, True),
    ),
])
