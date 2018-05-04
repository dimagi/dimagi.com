from . import version_2, version_3


PREVIOUS_TERMS = (
    version_2.PRIVACY,
    version_2.EULA,
    version_2.PSA,
)


LATEST_TERMS = (
    version_3.PRIVACY,
    version_3.TOS,
    version_3.BA,
    version_3.AUP,
)


def get_term_by_slug(terms, slug):
    latest_by_slug = dict([(t.slug, t) for t in terms])
    return latest_by_slug[slug]


def get_terms_by_version(version):
    versions = {
        'previous': PREVIOUS_TERMS,
        'latest': LATEST_TERMS,
    }
    return versions[version]
