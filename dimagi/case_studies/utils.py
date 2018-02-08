from dimagi.case_studies.mhealth import studies as mhealth


def get_case_study_by_slug(slug):
    case_study_by_slug = dict((c.STUDY.slug, c.STUDY) for c in mhealth)
    return case_study_by_slug.get(slug)


def get_case_studies_page(page):
    studies = mhealth

    first_index = (page - 1) * 20
    last_index = max(first_index + 20, len(studies))

    if last_index > first_index:
        print(last_index)
        print(first_index)
        studies = studies[first_index:last_index]
        return [c.STUDY for c in studies]
