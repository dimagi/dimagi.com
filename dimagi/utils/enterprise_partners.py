

WEB = [
    [
        "svg/partner/enterprise/af.html",
        "svg/partner/enterprise/cf.html",
    ],
    [
        "svg/partner/enterprise/crs.html",
        "svg/partner/enterprise/goal.html",
    ],
    [
        "svg/partner/enterprise/irc.html",
        "svg/partner/enterprise/ss.html",
    ],
    [
        "svg/partner/enterprise/tf.html",
        "svg/partner/enterprise/ts.html",
    ],
    [
        "svg/partner/enterprise/wv.html",
        "svg/partner/enterprise/crs.html",
    ],
    [
        "svg/partner/enterprise/goal.html",
        "svg/partner/enterprise/ss.html",
    ],
]


MOBILE = [
    [
        "svg/partner/enterprise/af.html",
        "svg/partner/enterprise/cf.html",
        "svg/partner/enterprise/crs.html",
    ],
    [
        "svg/partner/enterprise/goal.html",
        "svg/partner/enterprise/irc.html",
    ],
    [
        "svg/partner/enterprise/ss.html",
        "svg/partner/enterprise/tf.html",
    ],
    [
        "svg/partner/enterprise/ts.html",
        "svg/partner/enterprise/wv.html",
    ],
]


def get_enterprise_partners():
    return {
        'mobile': MOBILE,
        'web': WEB,
    }
