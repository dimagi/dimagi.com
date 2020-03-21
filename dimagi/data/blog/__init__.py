from dimagi.data.blog.categories import (
    PRODUCT,
    PARTNERS,
    STAFF,
    ARCHIVE,
    TECH,
    PARTNERS_LATEST,
)


available_categories = (
    PRODUCT,
    PARTNERS,
    STAFF,
    ARCHIVE,
    TECH,
    PARTNERS_LATEST,
)


nav_categories = (
    PRODUCT,
    PARTNERS,
    STAFF,
    TECH,
)


def get_category_by_slug(slug):
    slug_to_cat = dict((c.slug, c) for c in available_categories)
    try:
        return slug_to_cat[slug]
    except KeyError:
        return ARCHIVE

