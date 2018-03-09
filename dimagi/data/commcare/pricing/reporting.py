from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
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
            "Pre-built reports"
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
            "Excel dashboard linking"
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
            "Case Importer"
        ),
        description=ugettext_lazy(
            "Create or update cases in bulk using Excel. With this feature, "
            "you can make changes or create new cases quickly and effectively. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Report Builder"
        ),
        description=ugettext_lazy(
            "Design and build your own reports based on data from your "
            "CommCare application. Publish reports or schedule emails to share "
            "reports with other users."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Data management"
        ),
        description=ugettext_lazy(
            "Use the features in our data management toolkit to ensure all "
            "data on CommCareHQ is clean and accurate. With these features you "
            "can edit erroneous form submissions and archive test data, "
            "leaving a virtual paper trail of your changes."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Custom reports access"
        ),
        description=ugettext_lazy(
            "Access to custom reports. Note that the actual development of "
            "custom reports through Dimagi is a separate cost. Organizations "
            "that want additional reporting capabilities beyond what is "
            "offered in standard reports can contract with Dimagi to develop "
            "custom reports. Dimagi’s team works with organizations’ project "
            "teams to clarify and define all reporting indicators and "
            "features requested. The reports are deployed to the specific "
            "project they were designed for, but not available to other "
            "domains. The actual development of custom reports would form "
            "part of a Service Package and is not included in Software Plans."
        ),
        support=Support(False, True, True, True),
    ),
])
