from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Security and Compliance"
    ),
    slug='security-compliance',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Two-factor authentication"
        ),
        description=ugettext_lazy(
            "Turn on two-factor authentication for your web user to add a "
            "second level of authentication and make your account more secure. "
            "For projects on Advanced plans, you can enforce two-factor "
            "authentication for all members of your project."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Data de-identification"
        ),
        description=ugettext_lazy(
            "Mark a data point as 'identifying' and the export tool will "
            "randomly transform the data during export. This is useful for "
            "projects collecting health data that need to de-identify a "
            "dataset to meet privacy requirements."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Security policy control and enforcement"
        ),
        description=ugettext_lazy(
            "Enforce stronger account security for web and mobile user "
            "accounts in your project. Require two-factor authentication "
            "for web users and strong passwords for mobile workers."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "HIPAA compliance assurance"
        ),
        description=ugettext_lazy(
            "You might prefer or require HIPAA compliance if you are "
            "concerned about having the highest standards of security "
            "regarding your projects' personal health information. Standard "
            "hosting is also secure, but not signed off as officially "
            "compliant with HIPAA certified hosting. Under the Advanced "
            "and above plans, Dimagi ensures that all data that is collected "
            "and hosted on CommCareHQ meets the essential security and "
            "availability requirements for HIPAA compliance. Dimagi also "
            "gives access to signing a HIPAA Business Associate Agreement "
            "(BAA) for the Advanced and above plans."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Customized GDPR Data Processing Agreement"
        ),
        description=ugettext_lazy(
            "We are fully GPDR Complaint, and offer Data Processing "
            "Agreements on all plans. We offer customizations to our "
            "standardized DPA only on your Advanced plan. This is primarily "
            "because customizations creates additional and permanent overhead "
            "on our multiple teams."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Customized product terms"
        ),
        description=mark_safe(ugettext_lazy("""Check here for our 
        <a href="https://www.dimagi.com/terms/latest/tos/"
           target="_blank">Terms</a>. 
        Our Terms consist of our Terms of Service, Privacy Policy, Business 
        Agreement, and Acceptable Usage Policy. We offer reasonable customizations 
        to our Terms only on our Advanced plan. This is primarily because 
        customizations creates additional and permanent 
        overhead on our multiple teams. 
        """)),
        support=Support(False, False, True, True),
    ),
])
