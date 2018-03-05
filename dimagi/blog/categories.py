from __future__ import absolute_import
from collections import namedtuple

from django.utils.translation import ugettext_lazy

Category = namedtuple('Category', 'name description slug')

PRODUCT = Category(
    name=ugettext_lazy("Product Updates"),
    description=ugettext_lazy(
        "All of the newest CommCare<br />"
        "feature updates."
    ),
    slug="product",
)

PARTNERS = Category(
    name=ugettext_lazy("Dimagi Partner Blog"),
    description=ugettext_lazy(
        "Read for the latest news and stories<br />"
        "from our Partners around the world."
    ),
    slug="partners",
)

STAFF = Category(
    name=ugettext_lazy("Staff Blog"),
    description=ugettext_lazy(
        "Dimagi staff offer their insights on<br />"
        "app-building and more."
    ),
    slug="staff",
)

TECH = Category(
    name=ugettext_lazy("Technology"),
    description=ugettext_lazy(
        "Members of our tech team share insights<br />"
        "about technologies we use for CommCare."
    ),
    slug="tech",
)

ARCHIVE = Category(
    name=ugettext_lazy("Archive"),
    description=ugettext_lazy(
        "The intersection of technology<br />and social good."
    ),
    slug="archive",
)


def get_category_by_slug(slug):
    slug_to_cat = dict((c.slug, c) for c in [
        PRODUCT,
        PARTNERS,
        STAFF,
        ARCHIVE,
        TECH,
    ])
    try:
        return slug_to_cat[slug]
    except KeyError:
        return ARCHIVE
