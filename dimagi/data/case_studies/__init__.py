from dimagi.data.case_studies.mhealth import studies


def get_case_study_by_slug(slug):
    case_study_by_slug = dict((c.STUDY.slug, c.STUDY) for c in studies)
    return case_study_by_slug.get(slug)


def get_case_studies_page(page):
    first_index = (page - 1) * 20
    last_index = max(first_index + 20, len(studies))

    if last_index > first_index:
        page_studies = studies[first_index:last_index]
        return [c.STUDY for c in page_studies]
