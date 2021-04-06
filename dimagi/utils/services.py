

WEB = [
    [
        "svg/partner/services/tdh.html",
        "svg/partner/services/abt.html",
        "svg/partner/services/acdi_voca.html",
    ],
    [
        "svg/partner/services/bmgf.html",
        "svg/partner/services/cdc.html",
    ],
    [
        "svg/partner/services/dai.html",
        "svg/partner/services/fhi.html",
    ],
    [
        "svg/partner/services/find.html",
        "svg/partner/services/hki.html",
    ],
    [
        "svg/partner/services/idb.html",
        "svg/partner/services/jsi.html",
    ],
    [
        "svg/partner/services/msh.html",
        "svg/partner/services/uncdf.html",
    ],
]


MOBILE = [
    [
        "svg/partner/services/abt.html",
        "svg/partner/services/acdi_voca.html",
        "svg/partner/services/bmgf.html",
        "svg/partner/services/cdc.html",
    ],
    [
        "svg/partner/services/dai.html",
        "svg/partner/services/fhi.html",
        "svg/partner/services/find.html",
    ],
    [
        "svg/partner/services/hki.html",
        "svg/partner/services/idb.html",
        "svg/partner/services/jsi.html",
    ],
    [
        "svg/partner/services/msh.html",
        "svg/partner/services/tdh.html",
        "svg/partner/services/uncdf.html",
    ],
]


def get_service_partners():
    return {
        'mobile': MOBILE,
        'web': WEB,
    }
