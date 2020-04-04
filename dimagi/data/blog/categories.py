from __future__ import absolute_import

from django.utils.translation import ugettext_lazy

from dimagi.pages.models.blog import Category


PRODUCT = Category(
    name=ugettext_lazy("Product Updates"),
    description=ugettext_lazy(
        "All of the newest CommCare<br />"
        " feature updates."
    ),
    icon="svg/blog/icon/product.html",
    slug="product",
)

PARTNERS = Category(
    name=ugettext_lazy("Dimagi Partner Blog"),
    description=ugettext_lazy(
        "Read for the latest news and stories<br />"
        " from our Partners around the world."
    ),
    icon="svg/blog/icon/partners.html",
    slug="partners",
)

STAFF = Category(
    name=ugettext_lazy("Staff Blog"),
    description=ugettext_lazy(
        "Dimagi staff offer their insights on<br />"
        " app building and more."
    ),
    icon="svg/blog/icon/staff.html",
    slug="staff",
)

TECH = Category(
    name=ugettext_lazy("Technology"),
    description=ugettext_lazy(
        "Members of our tech team share insights<br />"
        " about technologies we use for CommCare."
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

PARTNERS_LATEST = Category(
    name=ugettext_lazy("Dimagi New Projects"),
    description=ugettext_lazy(
        "Read about new projects we’re working on "
        "around the world with our Partners."
    ),
    icon="svg/blog/icon/technology.html",
    slug="latest-partners",
)

COVID_19 = Category(
    name=ugettext_lazy("COVID-19"),
    description=ugettext_lazy(
        "Updates for Dimagi's COVID-19 initiatives."
    ),
    icon="svg/blog/icon/technology.html",
    slug="covid-19",
)
