

WEB = [
    [
        "svg/partner/india/usaid.html",
    ],
    [
        "svg/partner/india/tdh.html",
    ],
    [
        "svg/partner/india/crs.html",
    ],
    [
        "svg/partner/india/gates.html",
    ],
    [
        "svg/partner/india/ipe.html",
    ],
    [
        "svg/partner/india/pathfinder.html",
        "svg/partner/india/jnj.html",
    ],
]


MOBILE = [
    [
        "svg/partner/india/usaid.html",
        "svg/partner/india/pathfinder.html",
    ],
    [
        "svg/partner/india/tdh.html",
        "svg/partner/india/jnj.html",
    ],
    [
        "svg/partner/india/crs.html",
        "svg/partner/india/usaid.html",
    ],
    [
        "svg/partner/india/gates.html",
        "svg/partner/india/usaid.html",
    ],
]


def get_india_partners():
    return {
        'mobile': MOBILE,
        'web': WEB,
    }
