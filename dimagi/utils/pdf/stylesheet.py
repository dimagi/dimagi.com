from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.fonts import tt2ps
from reportlab.lib.styles import StyleSheet1, ParagraphStyle


class CommCareStyle(object):
    DEFAULT_FONT = "Helvetica"
    BOLD_FONT = tt2ps(DEFAULT_FONT, 1, 0)

    COLOR_BLUE_DARK = HexColor(0x002C5F)
    COLOR_TEXT = HexColor(0x5F6A7D)
    COLOR_ACCENT_GRAY = HexColor(0xFAFAFA)
    COLOR_BORDER = HexColor(0xE0E0E0)
    COLOR_WHITE = HexColor(0xFFFFFF)
    COLOR_GREEN = HexColor(0x47B700)
    COLOR_BLUE = HexColor(0x004EBC)
    COLOR_TURQUOISE = HexColor(0x00BDC5)
    COLOR_PURPLE = HexColor(0x9060C8)

    SIZE_H1 = 20
    SIZE_H2 = 14
    SIZE_H3 = 12
    SIZE_NORMAL = 10
    SIZE_SMALL = 8

    LINE_HEIGHT_H1 = 40
    LINE_HEIGHT_H2 = 24
    LINE_HEIGHT_NORMAL = 14
    LINE_HEIGHT_SMALL = 12

    def __init__(self):
        self.stylesheet = StyleSheet1()

        self.stylesheet.add(
            ParagraphStyle(
                name='title',
                fontName=self.DEFAULT_FONT,
                fontSize=self.SIZE_H1,
                leading=self.LINE_HEIGHT_H1,
                textTransform='uppercase',
            )
        )

        self.stylesheet.add(
            ParagraphStyle(
                name='price',
                fontName=self.BOLD_FONT,
                fontSize=self.SIZE_H2,
                leading=self.LINE_HEIGHT_H2 - 8,
                textColor=self.COLOR_TEXT,
                alignment=TA_CENTER,

            )
        )
        self.stylesheet.add(
            ParagraphStyle(
                name='header',
                fontName=self.DEFAULT_FONT,
                fontSize=self.SIZE_H2,
                leading=self.LINE_HEIGHT_H2,
                textTransform='uppercase',
            )
        )
        self.create_plan_headers()

        self.stylesheet.add(
            ParagraphStyle(
                name='footer',
                fontName=self.DEFAULT_FONT,
                fontSize=self.SIZE_H2,
                leading=self.LINE_HEIGHT_H2,
                textColor=self.COLOR_TEXT,
                alignment=TA_CENTER,
            )
        )

        self.stylesheet.add(
            ParagraphStyle(
                name='pay-type',
                fontName=self.BOLD_FONT,
                fontSize=self.SIZE_SMALL,
                leading=self.SIZE_SMALL + 2,
                alignment=TA_CENTER,
                textTransform='uppercase',
                borderPadding=2,
            )
        )
        self.create_pay_types()

        self.create_detail()

        self.stylesheet.add(
            ParagraphStyle(
                name='normal',
                alias='p',
                fontName=self.DEFAULT_FONT,
                fontSize=self.SIZE_NORMAL,
                leading=self.LINE_HEIGHT_NORMAL,
                textColor=self.COLOR_TEXT
            )
        )

        self.stylesheet.add(
            ParagraphStyle(
                'normal-centered',
                alias='p-center',
                parent=self.stylesheet['normal'],
                alignment=TA_CENTER,
            )
        )

    @property
    def _plan_colors(self):
        return {
            'standard': self.COLOR_GREEN,
            'pro': self.COLOR_TURQUOISE,
            'advanced': self.COLOR_PURPLE,
            'enterprise': self.COLOR_BLUE,
        }

    def create_plan_headers(self):
        for plan, color in self._plan_colors.items():
            self.stylesheet.add(
                ParagraphStyle(
                    'header-{}'.format(plan),
                    parent=self.stylesheet['header'],
                    alignment=TA_CENTER,
                    textColor=color,
                )
            )

    def create_pay_types(self):
        for plan, color in self._plan_colors.items():
            self.stylesheet.add(
                ParagraphStyle(
                    'pay-type-monthly-{}'.format(plan),
                    parent=self.stylesheet['pay-type'],
                    textColor=color,
                    borderColor=color,
                    borderWidth=1,
                )
            )
            self.stylesheet.add(
                ParagraphStyle(
                    'pay-type-annually-{}'.format(plan),
                    parent=self.stylesheet['pay-type'],
                    textColor=self.COLOR_WHITE,
                    backColor=color,
                )
            )

    def create_detail(self):
        for plan, color in self._plan_colors.items():
            self.stylesheet.add(
                ParagraphStyle(
                    'detail-{}'.format(plan),
                    fontName=self.BOLD_FONT,
                    fontSize=self.SIZE_SMALL,
                    leading=self.SIZE_SMALL,
                    alignment=TA_CENTER,
                    textTransform='uppercase',
                    textColor=color,
                )
            )

    @property
    def title(self):
        return self.stylesheet['title']

    @property
    def footer(self):
        return self.stylesheet['footer']

    def plan_header(self, plan):
        return self.stylesheet['header-{}'.format(plan)]

    def pay_type(self, pay_type, plan):
        return self.stylesheet['pay-type-{}-{}'.format(pay_type, plan)]

    @property
    def price(self):
        return self.stylesheet['price']

    def detail(self, plan):
        return self.stylesheet['detail-{}'.format(plan)]

    @property
    def normal(self):
        return self.stylesheet['normal']

    @property
    def normal_center(self):
        return self.stylesheet['normal-centered']
