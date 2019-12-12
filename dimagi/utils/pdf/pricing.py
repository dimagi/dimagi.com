from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division
import os
from tempfile import NamedTemporaryFile

from django.utils.encoding import force_text
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Spacer,
    PageBreak,
    Flowable,
    Table,
    TableStyle,
)
from reportlab.lib.pagesizes import letter

from dimagi.utils.pdf.stylesheet import CommCareStyle

HEADER_IMAGE_FILEPATH = "assets/images/pricing-pdf-header.jpg"


def inches(num_inches):
    return inch * num_inches


CENTER_X = inches(4.25)


class PricingDocTemplate(BaseDocTemplate):

    def __init__(self, filename):
        super(PricingDocTemplate, self).__init__(
            filename,
            pageTemplates=[
                OverviewPageTemplate(),
                ComparisonPageTemplate(),
            ],
            pagesize=letter,
            title="CommCare Pricing",
            author="Dimagi, Inc.",
        )

    def handle_pageBegin(self):
        self._handle_pageBegin()
        self._handle_nextPageTemplate('Comparison')


class OverviewPageTemplate(PageTemplate):

    def __init__(self):
        margin = .5
        space = .18
        width = (8.5 - margin * 2 - space * 3) / 4.

        frames = []
        for num in range(4):
            x = margin + (space * num) + (width * num)
            frames.append(Frame(
                inches(x),
                inches(0.95),
                inches(width),
                inches(3.15),
                leftPadding=inches(.24),
                rightPadding=inches(.24)
            ))

        super(OverviewPageTemplate, self).__init__(
            id="First",
            frames=frames
        )

    def beforeDrawPage(self, canvas, doc):
        # header image
        canvas.drawImage(
            os.path.join(os.getcwd(), HEADER_IMAGE_FILEPATH),
            0,
            inches(1.0),
            width=inches(8.5),
            preserveAspectRatio=True
        )

        # heading text
        canvas.setFillColor(CommCareStyle.COLOR_BLUE_DARK)
        canvas.setFont(CommCareStyle.DEFAULT_FONT, CommCareStyle.SIZE_H1)
        canvas.drawCentredString(
            CENTER_X,
            inches(6.4),
            "COMMCARE PRICING"
        )

        # tagline
        canvas.setFillColor(CommCareStyle.COLOR_TEXT)
        canvas.setFont(CommCareStyle.DEFAULT_FONT, CommCareStyle.SIZE_NORMAL)
        canvas.drawCentredString(
            CENTER_X,
            inches(6),
            "Get the features you need at an affordable price"
        )
        canvas.drawCentredString(
            CENTER_X,
            inches(5.8),
            "with our flexible plans, designed for projects of all sizes."
        )

        # gray BG
        canvas.setFillColor(CommCareStyle.COLOR_ACCENT_GRAY)
        canvas.rect(
            inches(0), inches(0.0), inches(8.5), inches(5.25), fill=1, stroke=0
        )

        # gray top border of BG
        canvas.setStrokeColor(CommCareStyle.COLOR_BORDER)
        canvas.setLineWidth(1)
        canvas.line(inches(0), inches(5.25), inches(8.5), inches(5.25))

        # price boxes (standard, pro, advanced, enterprise)
        margin = .5
        space = .18
        width = (8.5 - margin * 2 - space * 3) / 4.
        canvas.setFillColor(CommCareStyle.COLOR_WHITE)
        colors = [
            CommCareStyle.COLOR_GREEN,
            CommCareStyle.COLOR_TURQUOISE,
            CommCareStyle.COLOR_PURPLE,
            CommCareStyle.COLOR_BLUE,
        ]

        for num in range(4):
            x = margin + (space * num) + (width * num)
            canvas.setStrokeColor(colors[num])
            canvas.roundRect(
                inches(x),
                inches(.55),
                inches(width),
                inches(4.),
                inches(.2),
                fill=1,
                stroke=1
            )

        # most popular plan circle
        canvas.setFillColor(CommCareStyle.COLOR_TURQUOISE)
        canvas.circle(inches(2.65), inches(4.55), inches(.35), fill=1, stroke=0)

        # most popular plan text
        canvas.setFillColor(CommCareStyle.COLOR_WHITE)
        canvas.setFont(CommCareStyle.BOLD_FONT, CommCareStyle.SIZE_SMALL)
        canvas.drawCentredString(inches(2.65), inches(4.66), "MOST")
        canvas.drawCentredString(inches(2.65), inches(4.51), "POPULAR")
        canvas.drawCentredString(inches(2.65), inches(4.36), "PLAN")


class FeatureGroupHeader(Flowable):

    def __init__(self, title):
        super(FeatureGroupHeader, self).__init__()
        self.title = force_text(title)
        self.width = inches(7.5)
        self.height = inches(.5)

    def wrap(self, *args):
        return self.width, self.height

    def draw(self):
        self.canv.setFillColor(CommCareStyle.COLOR_TEXT)
        self.canv.rect(
            inches(0),
            inches(0),
            self.width,
            self.height,
            fill=1,
            stroke=0,
        )

        self.canv.setFont(CommCareStyle.DEFAULT_FONT, CommCareStyle.SIZE_H3)
        self.canv.setFillColor(CommCareStyle.COLOR_WHITE)
        self.canv.drawString(inches(.2), inches(.2), self.title)


class FeatureLine(Flowable):

    def __init__(self, title, support):
        super(FeatureLine, self).__init__()
        self.title = force_text(title)
        self.support = support
        self.width = inches(7.5)
        self.height = inches(.5)
        self.x = list(map(lambda x: inches(3.2 + 1.2 * x), range(4)))
        self.Y = list(map(lambda Y: inches(3.2 + 1.2 * Y), range(4)))
        self._style = CommCareStyle()

    def wrap(self, *args):
        return self.width, self.height

    def _draw_value(self, x, Y, color, value, slug):
        self.canv.setFillColor(color)
        self.canv.setStrokeColor(color)
        self.canv.setLineWidth(1.5)
        if not isinstance(value, bool):
            value = force_text(value)
            value = value.upper()
            p = Paragraph(value, self._style.detail(slug))
            t = Table([[p]], [inches(1)], [inches(.5)])
            t.setStyle(TableStyle([('VALIGN', (0, -1), (-1, -1), 'MIDDLE')]))
            t.wrapOn(self.canv, inches(1), inches(.5))
            t.drawOn(self.canv, x - inches(.55), inches(0.01))
            t.drawOn(self.canv, Y - inches(.55), inches(0.01))
        elif value:
            self.canv.line(
                x - inches(.06),
                inches(.25),
                Y - inches(-.01),
                inches(.21)
            )
            self.canv.line(
                x + inches(.00),
                inches(.21),
                Y + inches(.12),
                inches(.33)
            )
        else:
            self.canv.line(
                x - inches(.06),
                inches(.25),
                x + inches(.06),
                inches(.25)
            )

    def draw(self):
        p = Paragraph(self.title, self._style.normal)
        t = Table([[p]], [inches(2.5)], [inches(.5)])
        t.setStyle(TableStyle([('VALIGN', (0, -1), (-1, -1), 'MIDDLE')]))
        t.wrapOn(self.canv, inches(2.5), inches(.5))
        t.drawOn(self.canv, inches(0.1), inches(0.01))

        self._draw_value(
            self.x[0],
            self.Y[0],
            CommCareStyle.COLOR_GREEN,
            self.support.standard,
            'standard'
        )

        self._draw_value(
            self.x[1],
            self.Y[1],
            CommCareStyle.COLOR_TURQUOISE,
            self.support.pro,
            'pro'
        )

        self._draw_value(
            self.x[2],
            self.Y[2],
            CommCareStyle.COLOR_PURPLE,
            self.support.advanced,
            'advanced'
        )

        self._draw_value(
            self.x[3],
            self.Y[3],
            CommCareStyle.COLOR_BLUE,
            self.support.enterprise,
            'enterprise'
        )


class ComparisonPageTemplate(PageTemplate):

    def __init__(self):
        super(ComparisonPageTemplate, self).__init__(
            id="Comparison",
            frames=[
                Frame(
                    inches(.5),
                    inches(.6),
                    inches(7.5),
                    inches(8.75),
                    leftPadding=0,
                    rightPadding=0,
                    topPadding=0,
                    bottomPadding=0,
                ),
            ]
        )

    def beforeDrawPage(self, canvas, doc):
        # heading text
        canvas.setFillColor(CommCareStyle.COLOR_BLUE_DARK)
        canvas.setFont(CommCareStyle.DEFAULT_FONT, CommCareStyle.SIZE_H1)
        canvas.drawCentredString(
            CENTER_X,
            inches(10.25),
            "DETAILED COMPARISON"
        )

        start = 3.7
        delta = 1.2

        headings = (
            ("STANDARD", CommCareStyle.COLOR_GREEN),
            ("PRO", CommCareStyle.COLOR_TURQUOISE),
            ("ADVANCED", CommCareStyle.COLOR_PURPLE),
            ("ENTERPRISE", CommCareStyle.COLOR_BLUE),
        )

        canvas.setFont(CommCareStyle.DEFAULT_FONT, CommCareStyle.SIZE_H3)

        for num in range(4):
            canvas.setFillColor(headings[num][1])
            canvas.drawCentredString(
                inches(start + delta * num),
                inches(9.6),
                headings[num][0]
            )


def _fmt_price(monthly, annually):
    return {
        'monthly': monthly,
        'annually': annually,
    }


def _get_plan(style, name, description, price, pay_type):
    return [
        Paragraph(name, style.plan_header(name)),
        Spacer(1, 2),
        Paragraph(
            "paying {}".format(pay_type),
            style.pay_type(pay_type, name)
        ),
        Spacer(1, 10),
        Paragraph(price[pay_type], style.price),
        Paragraph("monthly", style.normal_center),
        Spacer(1, 12),
        Paragraph(description, style.normal_center),
    ]


def get_pricing_pdf(groups, is_monthly=False):
    data = NamedTemporaryFile()
    style = CommCareStyle()
    doc = PricingDocTemplate(data.name)

    pay_type = 'monthly' if is_monthly else "annually"

    story = []

    story.extend(_get_plan(
        style,
        "standard",
        "For programs with one-time data collection needs, simple "
        "case management workflows, and basic M&E requirements.",
        _fmt_price("$300", "$250"),
        pay_type
    ))

    story.extend(_get_plan(
        style,
        "pro",
        "For programs with complex case management needs, field "
        "staff collaborating on tasks, and M&E teams that "
        "need to clean and report on data.",
        _fmt_price("$600", "$500"),
        pay_type
    ))

    story.extend(_get_plan(
        style,
        "advanced",
        "For programs with facility-based workflows, distributed field staff, and "
        "advanced security needs. Also for M&E teams integrating "
        "data with 3rd party analytics.",
        _fmt_price("$1200", "$1000"),
        pay_type
    ))

    story.extend(_get_plan(
        style,
        "enterprise",
        "For organizations that need a sustainable path to scale "
        "mobile data collection and service delivery across "
        "multiple teams, programs, or countries.",
        _fmt_price("Contact Us", "Contact Us"),
        pay_type
    ))

    story.append(PageBreak())

    for group in groups:
        story.append(FeatureGroupHeader(group.title))
        for feature in group.features:
            story.append(FeatureLine(
                feature.title,
                feature.support
            ))

    story.append(Spacer(1, 30))
    story.append(Paragraph(
        "Want to learn more? Contact our sales team at sales@dimagi.com.",
        style.footer
    ))

    doc.build(story)
    return data
