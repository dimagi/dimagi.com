from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.quick_start import QuickStartCard


GET_STARTED = QuickStartCard(
    icon="svg/quick_start/a_video.html",
    title=ugettext_lazy("Get started with CommCare"),
    description=ugettext_lazy("""
    So many apps, so little time&mdash;quickly learn the basics of CommCare 
    with our video series.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://www.youtube.com/watch?v=ng4zGf1PGxM"
        "&list=PLVmwIEfrcKqkZsRuWVXL-Djsj2JlROvpU"
)


BECOME_A_PRO = QuickStartCard(
    icon="svg/quick_start/a_pro.html",
    title=ugettext_lazy("Become a CommCare Pro"),
    description=ugettext_lazy("""
    Join our Academy team as they walk you through the essential steps of 
    CommCare app building.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://academy.dimagi.com/"
)


REVIEW_APP = QuickStartCard(
    icon="svg/quick_start/a_review.html",
    title=ugettext_lazy("Review your app with us"),
    description=ugettext_lazy("""
    Every program’s needs are unique. Book a personal consultation to talk 
    through your specific requirements.
    """),
    level=ugettext_lazy("Beginner"),
    cta="http://sites.dimagi.com/commcare-app-review"
)


CONTACT_SUPPORT = QuickStartCard(
    icon="svg/quick_start/a_support.html",
    title=ugettext_lazy("Contact Support"),
    description=ugettext_lazy("""
    Running into an issue? Receive help with specific features and troubleshoot 
    our app.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://www.dimagi.com/contact/"
)


EXPORT_DATA_FOR_ANALYSIS = QuickStartCard(
    title=ugettext_lazy("Export data for analysis"),
    icon="svg/quick_start/b_export.html",
    description=ugettext_lazy("""
    Access data collected with your app and export for use in any 
    third-party analytics tool.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/"
        "commcarepublic/Data+Export+Overview"
)


MONITOR_CHANGES_OVER_TIME = QuickStartCard(
    title=ugettext_lazy("Monitor changes over time"),
    icon="svg/quick_start/b_monitor.html",
    description=ugettext_lazy("""
    Track and analyze the status of your cases&mdash;people, farms, or anything 
    else&mdash;over a period of time.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Case+Management"
)


AUTOMATE_YOUR_REPORTS = QuickStartCard(
    title=ugettext_lazy("Automate your reports"),
    icon="svg/quick_start/b_automate.html",
    description=ugettext_lazy("""
    Spend your time drawing insights from data, not on backend administration, 
    with daily saved exports.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Daily+Saved+Exports"
)


MONITOR_YOUR_WORKFORCE = QuickStartCard(
    title=ugettext_lazy("Monitor your workforce"),
    icon="svg/quick_start/bc_dashboard.html",
    description=ugettext_lazy("""
    Quickly view and evaluate the performance of your field team.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Worker+Monitoring+Reports"
)


LINK_TO_EXCEL_DASHBOARDS = QuickStartCard(
    title=ugettext_lazy("Link your data to Excel dashboards"),
    icon="svg/quick_start/b_link.html",
    description=ugettext_lazy("""
    Never worry about stale reports again by connecting your CommCare data 
    directly to Excel dashboards.
    """),
    level=ugettext_lazy("Advanced"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Tutorial%3A+Create+an+Excel+Dashboard"
)


INSPECT_YOUR_DATA = QuickStartCard(
    title=ugettext_lazy("Inspect your data"),
    icon="svg/quick_start/b_inspect.html",
    description=ugettext_lazy("""
    View individual form submissions and case data to check for errors or 
    inconsistencies in your data.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Inspect+Data"
)


CORRECT_DATA_ERRORS = QuickStartCard(
    title=ugettext_lazy("Correct data errors"),
    icon="svg/quick_start/b_correct.html",
    description=ugettext_lazy("""
    Edit your case data—both properties and specific values&mdash;without ever 
    leaving CommCare.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Data+Corrections%3A+Edit+Case+Data"
)


ELIMINATE_DUPLICATE_DATA = QuickStartCard(
    title=ugettext_lazy("Eliminate duplicate data"),
    icon="svg/quick_start/bd_duplicate.html",
    description=ugettext_lazy("""
    Minimize data errors with a prescribed workflow for your field workers.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/pages/viewpage.action?pageId=30605985"
)


HELP_APP_BUILDERS = QuickStartCard(
    title=ugettext_lazy("Help your app builders help themselves"),
    icon="svg/quick_start/b_help.html",
    description=ugettext_lazy("""
    Provide self-service learning for your stakeholders with CommCare 
    App Building tutorials.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Application+Building"
)


TECH_SUPPORT = QuickStartCard(
    title=ugettext_lazy("Provide top-notch tech support"),
    icon="svg/quick_start/b_tech_support.html",
    description=ugettext_lazy("""
    Learn how to manage your CommCare apps and avoid issues with our Technical 
    Support Learning Track.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Technical+Support+Learning+Track+-+Android"
)


TROUBLESHOOT_APPS = QuickStartCard(
    title=ugettext_lazy("Troubleshoot apps with ease"),
    icon="svg/quick_start/b_troubleshoot.html",
    description=ugettext_lazy("""
    Breeze through technical challenges using our FAQ guide for troubleshooting 
    and implementation.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Troubleshooting"
)


COMMUNITY = QuickStartCard(
    title=ugettext_lazy("Tap our active user community"),
    icon="svg/quick_start/b_community.html",
    description=ugettext_lazy("""
    Need advice from like minded data collectors? Get tips and answer questions 
    on the CommCare forum.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://forum.dimagi.com/"
)


CUSTOMIZE_ACCESS = QuickStartCard(
    title=ugettext_lazy("Customize mobile user access"),
    icon="svg/quick_start/c_customize.html",
    description=ugettext_lazy("""
    Filter the content of your CommCare app based on specific user properties.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Form+Display+Conditions"
)


SHARE_CASES = QuickStartCard(
    title=ugettext_lazy("Share cases between field workers"),
    icon="svg/quick_start/c_share.html",
    description=ugettext_lazy("""
    Enable your field team to share responsibilities of a case load.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Case+Sharing"
)


TRIGGER_SMS_REMINDERS = QuickStartCard(
    title=ugettext_lazy("Trigger SMS reminders"),
    icon="svg/quick_start/c_trigger.html",
    description=ugettext_lazy("""
    Intelligently notify field workers when tasks are required or overdue.
    """),
    level=ugettext_lazy("Advanced"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Messaging+Beginner+Tutorial"
)


GUIDE_FIELD_WORKERS = QuickStartCard(
    title=ugettext_lazy("Guide your field workers"),
    icon="svg/quick_start/c_guide.html",
    description=ugettext_lazy("""
    Send data collectors to a specific screen in your app after submitting data.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "End+of+Form+Navigation"
)


SEND_DATA = QuickStartCard(
    title=ugettext_lazy("Send data to any application"),
    icon="svg/quick_start/c_integration.html",
    description=ugettext_lazy("""
    Use Zapier’s self-service workflows to integrate your CommCare data with 
    any application.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Zapier+Integration"
)


COLLECT_DATA = QuickStartCard(
    title=ugettext_lazy("Collect data in your web browser"),
    icon="svg/quick_start/c_collect.html",
    description=ugettext_lazy("""
    Utilize CommCare’s Web Apps to collect data from any web browser with an 
    internet connection.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Web+Apps"
)


CONTROL_ACCESS = QuickStartCard(
    title=ugettext_lazy("Control access with user management"),
    icon="svg/quick_start/c_manage.html",
    description=ugettext_lazy("""
    Easily manage every CommCare user in your organization, from field workers 
    to app builders.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/User+Management"
)


ADD_ONS = QuickStartCard(
    title=ugettext_lazy("Employ add-ons for more power"),
    icon="svg/quick_start/c_add_ons.html",
    description=ugettext_lazy("""
    Meet any stakeholder demand with a library of feature add-ons.
    """),
    level=ugettext_lazy("Advanced"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Add-Ons+and+Feature+Previews"
)


MULTIMEDIA = QuickStartCard(
    title=ugettext_lazy("Communicate better with multimedia"),
    icon="svg/quick_start/d_multimedia.html",
    description=ugettext_lazy("""
    Add counseling messages, images, and videos to your app to help frontline 
    workers deliver better services.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Multimedia+in+CommCare"
)


EMPOWER_WITH_DATA = QuickStartCard(
    title=ugettext_lazy("Empower your field team with data"),
    icon="svg/quick_start/d_empower.html",
    description=ugettext_lazy("""
    Allow field workers to view case-related data right on their mobile device
    &mdash;even when offline.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Case+List+and+Case+Detail+Configuration"
)


PERFORM_BACKGROUND_CALCULATIONS = QuickStartCard(
    title=ugettext_lazy("Perform background calculations"),
    icon="svg/quick_start/d_workflow.html",
    description=ugettext_lazy("""
    Use Calculations, Display Conditions, and Logic to gather better data and 
    reduce burden on your frontline workers.
    """),
    level=ugettext_lazy("Advanced"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Common+Logic+and+Calculations"
)


AUTOMATE_YOUR_REFERRALS = QuickStartCard(
    title=ugettext_lazy("Automate your referrals"),
    icon="svg/quick_start/d_referral.html",
    description=ugettext_lazy("""
    Empower field workers to refer their cases to a specialist or alert a 
    program supervisor.
    """),
    level=ugettext_lazy("Advanced"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Referrals+in+CommCare"
)


BUILD_DYNAMIC_FORMS = QuickStartCard(
    title=ugettext_lazy("Build dynamic forms"),
    icon="svg/quick_start/d_build.html",
    description=ugettext_lazy("""
    Display content in your forms based on previous inputs.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Display+Conditions+Overview"
)


AUTOMATE_DATA_COLLECTION = QuickStartCard(
    title=ugettext_lazy("Automate data collection"),
    icon="svg/quick_start/d_automation.html",
    description=ugettext_lazy("""
    Let your app do the heavy lifting with Hidden Values.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/"
        "Hidden+Value+Calculations+Tutorial"
)


PRIORITIZE_TASKS = QuickStartCard(
    title=ugettext_lazy("Prioritize tasks for your field team"),
    icon="svg/quick_start/d_prioritize.html",
    description=ugettext_lazy("""
    Design your app to compliment existing workflows by sorting and filtering 
    content intelligently.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Menu+Filtering"
)


BUILD_CUSTOM_INTEGRATIONS = QuickStartCard(
    title=ugettext_lazy("Build custom integrations"),
    icon="svg/quick_start/d_integrations.html",
    description=ugettext_lazy("""
    Enable any integration with CommCare’s APIs, from programmatically 
    submitting data to automating your exports.
    """),
    level=ugettext_lazy("Advanced"),
    cta="https://confluence.dimagi.com/display/commcarepublic/CommCare+HQ+APIs"
)


MANAGE_ALL_YOUR_DATA = QuickStartCard(
    title=ugettext_lazy("Manage all your data"),
    icon="svg/quick_start/d_manage_data.html",
    description=ugettext_lazy("""
    Monitor activity and form submissions, manage exports, and prepare data 
    for your stakeholders.
    """),
    level=ugettext_lazy("Beginner"),
    cta="https://confluence.dimagi.com/display/commcarepublic/CommCare+Data"
)


TRUST_YOUR_INFRASTRUCTURE = QuickStartCard(
    title=ugettext_lazy("Trust your infrastructure"),
    icon="svg/quick_start/d_infrastructure.html",
    description=ugettext_lazy("""
    Get a technical overview of CommCare and learn why people trust the 
    platform for national-scale projects.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://docs.google.com/document/d/e/2PACX-1vRptqguFo-z4ip39yOHPt5uJ1"
        "-dajCHmLkRhRJhVZIT2BVpxv3ePuwAVMWkBjQVgfEe3qIHEy36uqB2/pub"
)


MANAGE_YOUR_DEVICES = QuickStartCard(
    title=ugettext_lazy("Manage your devices"),
    icon="svg/quick_start/d_devices.html",
    description=ugettext_lazy("""
    Using 100s&mdash;or even 1000s&mdash;of devices for data collection? 
    Get our mobile device management best-practices.
    """),
    level=ugettext_lazy("Intermediate"),
    cta="https://confluence.dimagi.com/display/commcarepublic/Phone+Management"
)
