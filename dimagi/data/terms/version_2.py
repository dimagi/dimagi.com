from django.utils.translation import ugettext_noop as _

from dimagi.pages.models.terms import (
    VERSION_2,
    Term
)


PRIVACY = Term(
    title=_("Privacy Policy"),
    slug='privacy',
    version=VERSION_2,
)


EULA = Term(
    title=_("End User License Agreement"),
    slug='eula',
    version=VERSION_2,
)


PSA = Term(
    title=_("Product Subscription Agreement"),
    slug='psa',
    version=VERSION_2,
)
