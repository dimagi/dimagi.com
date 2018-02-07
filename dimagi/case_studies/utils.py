from dimagi.case_studies.mhealth import (
    TDH_BURKINAFASO,
    LMRF_INDIA,
    MALARIA_MOZAMBIQUE,
    WORLD_VISION_MOTECH,
)


def get_case_study_by_slug(slug):
    case_studies = [
        TDH_BURKINAFASO,
        LMRF_INDIA,
        MALARIA_MOZAMBIQUE,
        WORLD_VISION_MOTECH,
    ]
    case_study_by_slug = dict((c.slug, c) for c in case_studies)
    return case_study_by_slug[slug]
