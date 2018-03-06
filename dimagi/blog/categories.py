from __future__ import absolute_import
from collections import namedtuple

from django.utils.translation import ugettext_lazy

Category = namedtuple('Category', 'name description icon slug')

PRODUCT = Category(
    name=ugettext_lazy("Product Updates"),
    description=ugettext_lazy(
        "All of the newest CommCare<br />"
        "feature updates."
    ),
    icon="svg/blog/icon/product.html",
    slug="product",
)

PARTNERS = Category(
    name=ugettext_lazy("Dimagi Partner Blog"),
    description=ugettext_lazy(
        "Read for the latest news and stories<br />"
        "from our Partners around the world."
    ),
    icon="svg/blog/icon/partners.html",
    slug="partners",
)

STAFF = Category(
    name=ugettext_lazy("Staff Blog"),
    description=ugettext_lazy(
        "Dimagi staff offer their insights on<br />"
        "app-building and more."
    ),
    icon="svg/blog/icon/staff.html",
    slug="staff",
)

TECH = Category(
    name=ugettext_lazy("Technology"),
    description=ugettext_lazy(
        "Members of our tech team share insights<br />"
        "about technologies we use for CommCare."
    ),
    icon="svg/blog/icon/technology.html",
    slug="tech",
)

ARCHIVE = Category(
    name=ugettext_lazy("Archive"),
    description=ugettext_lazy(
        "The intersection of technology<br />and social good."
    ),
    icon=None,
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
