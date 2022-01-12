from django.utils.translation import ugettext_noop as _

from dimagi.pages.models.terms import (
    VERSION_3,
    Term
)


PRIVACY = Term(
    title=_("Privacy Policy"),
    slug='privacy',
    version=VERSION_3,
)


TOS = Term(
    title=_("Terms of Service"),
    slug='tos',
    version=VERSION_3,
)


BA = Term(
    title=_("Business Agreement"),
    slug='ba',
    version=VERSION_3,
)


AUP = Term(
    title=_("Acceptable Use Policy"),
    slug='aup',
    version=VERSION_3,
)

FCI = Term(
    title=_("Financial Conflict of Interest"),
    slug='fci',
    version=VERSION_3,
)
