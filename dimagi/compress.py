from __future__ import absolute_import
from compressor.css import CssCompressor
from compressor.exceptions import UncompressableFileError
from compressor.filters.css_default import CssAbsoluteFilter
from django.core.files.base import ContentFile
from django.utils.safestring import mark_safe
from dimagi.utils.config import setting
from dimagi.utils.web import get_static_url


class S3CssCompressor(CssCompressor):

    def output_file(self, mode, content, forced=False, basename=None):
        """
        The output method that saves the content to a file and renders
        the appropriate template with the file's URL.
        """
        new_filepath = self.get_filepath(content, basename=basename)
        self.storage.local_storage.save(new_filepath, ContentFile(content.encode(self.charset)))
        url = get_static_url(mark_safe(new_filepath))
        return self.render_output(mode, {"url": url})

    def get_basename(self, url):
        try:
            base_url = self.storage.local_storage.base_url
        except AttributeError:
            base_url = setting('COMPRESS_URL', '')
        if not url.startswith(base_url):
            raise UncompressableFileError("'%s' isn't accessible via "
                                          "COMPRESS_URL ('%s') and can't be "
                                          "compressed" % (url, base_url))
        basename = url.replace(base_url, "", 1)
        # drop the querystring, which is used for non-compressed cache-busting.
        return basename.split("?", 1)[0]


class ImagekitCssAbsoluteFilter(CssAbsoluteFilter):

    def post_process_url(self, url):
        """
        Extra URL processing, to be overridden in subclasses.
        """
        # todo process url for image compressor
        return url
