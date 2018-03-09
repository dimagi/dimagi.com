from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Messaging (SMS / voice / email)"
    ),
    slug='messaging',
    description=mark_safe(ugettext_lazy("""
    Dimagi charges incoming and outgoing messages on a per-message fee. 
    <a href="https://www.commcarehq.org/messaging-pricing"
       target="_blank">View message rates</a>. 
    <a href="https://wiki.commcarehq.org/display/commcarepublic/CommCare+Messaging"
       target="_blank">Learn more about Messaging</a>.
    """)),
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "One-way messaging (SMS, email)"
        ),
        description=ugettext_lazy(
            "Configure outbound SMS systems that can be sent to both mobile "
            "workers and clients for broadcast messaging and targeted "
            "reminders."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Live SMS chat"
        ),
        description=ugettext_lazy(
            "Log into CommCareHQ and directly chat (over an IM interface) "
            "with mobile workers and clients."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Access Dimagi's in-country gateways"
        ),
        description=ugettext_lazy(
            "Sending and receiving automated SMS messages requires "
            "communicating with mobile networks. This is the job of SMS "
            "gateways. Dimagi’s SMS system comes with a gateway to a variety "
            "of countries worldwide. We provide a number of incoming and "
            "outgoing messages using our gateways included with each plan, "
            "Standard and above."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Android gateway setup"
        ),
        description=mark_safe(ugettext_lazy("""To establish SMS connectivity in 
        countries where we don't have our own SMS gateway set up, we offer 
        integration with Telerivet so that you can use your phone with 
        CommCareHQ to send and receive SMS to and from your project's 
        recipients. 
        <a href="https://wiki.commcarehq.org/display/commcarepublic/Setup+an+Android+SMS+Gateway"
           target="_blank">Learn more</a>.
        """)),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Two-way messaging (SMS, voice)"
        ),
        description=ugettext_lazy(
            "CommCare can be configured to support two-way messaging, which "
            "enables data collection over SMS or scheduling surveys to "
            "recipients using a rules engine."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Support to connect new in-country gateways"
        ),
        description=mark_safe(ugettext_lazy("""For larger high-volume projects 
        in countries we do not already support, Dimagi can support purchasing 
        and connecting a new 
        <a href="https://wiki.commcarehq.org/display/commcarepublic/Gateway+Options+for+SMS+Projects"
           target="_blank">gateway</a> to CommCareHQ. 
        """)),
        support=Support(False, False, True, True),
    ),
])
