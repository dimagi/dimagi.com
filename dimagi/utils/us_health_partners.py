

WEB = [
    [
        "svg/partner/ushealth/cdc.html",
        "svg/partner/ushealth/jhu.html",
    ],
    [
        "svg/partner/ushealth/usaid.html",
        "svg/partner/ushealth/ucsf.html",
    ],
    [
        "svg/partner/ushealth/nys.html",
        "svg/partner/ushealth/gates.html",
    ],
    [
        "svg/partner/ushealth/alaska.html",
        "svg/partner/ushealth/nj.html",
    ],
    [
        "svg/partner/ushealth/nih.html",
        "svg/partner/ushealth/pih.html",
    ],
]


MOBILE = [
    [
        "svg/partner/ushealth/cdc.html",
        "svg/partner/ushealth/ucsf.html",
    ],
    [
        "svg/partner/ushealth/nih.html",
        "svg/partner/ushealth/jhu.html",
        "svg/partner/ushealth/nj.html",
    ],
    [
        "svg/partner/ushealth/nys.html",
        "svg/partner/ushealth/gates.html",
    ],
    [
        "svg/partner/ushealth/alaska.html",
        "svg/partner/ushealth/usaid.html",
        "svg/partner/ushealth/pih.html",
    ],
]


def get_us_health_partners():
    return {
        'mobile': MOBILE,
        'web': WEB,
    }
