from __future__ import absolute_import
from dimagi.utils.config import setting


def is_production_environment():
    return setting('DEPLOY_ENVIRONMENT', '') == 'production'
