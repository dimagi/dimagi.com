from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Case Management"
    ),
    slug='case_management',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Basic case management"
        ),
        description=mark_safe(ugettext_lazy("""Basic 
    <a href="https://www.dimagi.com/case-management/"
    target="_blank">case management</a> enables users of the CommCare Mobile app 
    to register an entity (people, items of interest, etc.), then collect additional 
    data on that entity over time.
        """)),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Case sharing groups"
        ),
        description=mark_safe(ugettext_lazy("""
    <a href="https://confluence.dimagi.com/display/commcarepublic/Case+Sharing"
    target="_blank">Case sharing</a> allows groups of CommCare Mobile users to 
    access data from each other's cases. Case sharing is a powerful tool for 
    field teams that share data collection tasks across tracked entities. It 
    also enables referral workflows by allowing team members to view 
    and update shared cases.
        """)),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Child cases"
        ),
        description=mark_safe(ugettext_lazy("""
    <a href="https://confluence.dimagi.com/display/commcarepublic/Child+Cases"
    target="_blank">Child cases</a> enable you to open subcases linked to an 
    existing case. Child cases are useful for independently tracking linked 
    items, like a newborn that needs to be associated with its mother's 
    case but tracked separately.
        """)),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Location-based case sharing"
        ),
        description=mark_safe(ugettext_lazy("""Organize mobile workers according to the 
    <a href="https://confluence.dimagi.com/display/commcarepublic/Organizations"
    target="_blank">structure of your program</a>, enabling field staff to share 
    cases based on your program's specific organizational structure.
        """)),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Case List Explorer (CLE)"
        ),
        description=mark_safe(ugettext_lazy("""Case List Explorer is a powerful feature 
    for CommCare HQ which enables users to inspect their case data by building custom-filtered 
    views of their cases. The Case List Explorer allows you to find and validate test data, 
    identify cases that fit a very specific criteria, and find data anomalies and outlies.
        """)),
        support=Support(False, True, True, True),
    ),
])
