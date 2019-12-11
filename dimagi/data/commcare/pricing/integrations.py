from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "3rd Party Integrations"
    ),
    slug='integrations',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Zapier integration"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "CommCare Data Export Tool"
        ),
        description=ugettext_lazy(
            "The Data Export Tool is a command-line function that enables "
            "you to programatically pull form and case data from CommCare "
            "and save it locally (typically to either an Excel spreadsheet "
            "or a local database like MySQL). You can also run the Data "
            "Export Tool on a schedule to keep data fresh."
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
    Feature(
        title=ugettext_lazy(
            "API Access"
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Turnkey integration with 3rd party mobile apps"
        ),
        description=ugettext_lazy(
            "Integrate your CommCare application with other "
            "mobile apps like Simprints, Area Mapper, Breath "
            "Counter, and more—no coding required."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "External integration framework"
        ),
        description=ugettext_lazy(
            "CommCare's integration framework enables software developers "
            "to create custom integrations between CommCare "
            "Mobile and their own applications."
        ),
        support=Support(False, False, True, True),
    ),
])
