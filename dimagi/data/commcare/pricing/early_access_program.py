from django.utils.html import format_html
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)

EARLY_ACCESS_URL = "https://confluence.dimagi.com/display/commcarepublic/CommCare+Early+Access+Program"


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Early Access Program"
    ),
    slug='early_access_program',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Data Transformation Engine"
        ),
        description=format_html(ugettext_lazy(
            "Transform the data collected by your CommCare apps to create custom data sources. "
            "Consume the custom data sources for specific reporting and visualization needs like "
            "Supervisor Dashboards, M&E Indicator Reporting and more. "
            "Click <a href=\"{}\">here</a> to join our Early Access Program."
        ), EARLY_ACCESS_URL),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Mobile Reporting"
        ),
        description=format_html(ugettext_lazy(
            "Amplify the effectiveness of your programs by empowering your "
            "frontline staff with mobile reports on their CommCare app for "
            "enhanced decision support and effective case management. "
            "Click <a href=\"{}\">here</a> to join our Early Access Program."
        ), EARLY_ACCESS_URL),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Turnkey DHIS2 Integration"
        ),
        description=format_html(ugettext_lazy(
            "CommCare and DHIS2 work together to provide an end-to-end solution for mobile "
            "data collection and service delivery, aggregation, storage, and reporting at any "
            "scale—from a single community to nation-wide scale. CommCare now offers an in-product "
            "interface to configure the integration with your DHIS2 instance. "
            "Click <a href=\"{}\">here</a> to join our Early Access Program."
        ), EARLY_ACCESS_URL),
        support=Support(False, False, True, True),
    ),
])
