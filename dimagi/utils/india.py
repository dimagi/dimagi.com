

WEB = [
    [
        "svg/partner/usaid.html",
        "svg/partner/tdh.html",
    ],
    [
        "svg/partner/services/bmgf.html",
    ],
    [
        "svg/partner/tdh.html",
        "svg/partner/usaid.html",
    ],
    [
        "svg/partner/crs.html",
        "svg/partner/usaid.html",
    ],
    [
        "svg/partner/services/bmgf.html",
        "svg/partner/usaid.html",
    ],
    [
        "svg/partner/crs.html",
        "svg/partner/tdh.html",
    ],
]


MOBILE = [
    [
        "svg/partner/usaid.html",
        "svg/partner/tdh.html",
    ],
    [
        "svg/partner/services/bmgf.html",
    ],
    [
        "svg/partner/tdh.html",
        "svg/partner/usaid.html",
    ],
    [
        "svg/partner/crs.html",
        "svg/partner/usaid.html",
    ], 
]


def get_india_partners():
    return {
        'mobile': MOBILE,
        'web': WEB,
    }
