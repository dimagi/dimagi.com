from dimagi.data.toolkits import (
    total_cost_ownership,
    commcare_evidence_base,
    commcare_managing_data,
    managing_devices_ebook,
    data_collection,
    mobile_data_collection,
    digital_health_systems,
    digital_workflow_template,
)

toolkits = (
    total_cost_ownership,
    commcare_evidence_base,
    commcare_managing_data,
    managing_devices_ebook,
    data_collection,  
    mobile_data_collection,
    digital_health_systems,
    digital_workflow_template,
)


def get_toolkit_by_slug(slug):
    toolkit_by_slug = dict((t.TOOLKIT.slug, t.TOOLKIT) for t in toolkits)
    return toolkit_by_slug.get(slug)


def get_toolkits_page(page):
    first_index = (page - 1) * 20
    last_index = max(first_index + 20, len(toolkits))

    if last_index > first_index:
        page_toolkits = toolkits[first_index:last_index]
        return [t.TOOLKIT for t in page_toolkits]
