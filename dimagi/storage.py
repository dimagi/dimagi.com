from __future__ import absolute_import
from dimagi.utils.config import setting
from sass_processor.storage import SassS3Boto3Storage, SassFileStorage
from compressor.storage import CompressorFileStorage

STATIC_URL = setting('STATIC_URL', '')
STATIC_CDN = setting('STATIC_CDN', '')
CDN_BASE_URL = STATIC_CDN + STATIC_URL


class StaticFileStorage(SassFileStorage):
    pass


class S3BotoStorage(SassS3Boto3Storage):
    """
    S3 storage backend that has the right locations
    """
    location = STATIC_URL
    base_url = CDN_BASE_URL


class CompressedFileStorage(CompressorFileStorage):
    base_url = STATIC_URL
