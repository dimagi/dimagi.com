from __future__ import absolute_import
from compressor.css import CssCompressor
from django.core.files.base import ContentFile
from django.utils.safestring import mark_safe
from dimagi.utils.web import get_static_url


class S3CssCompressor(CssCompressor):

    def output_file(self, mode, content, forced=False, basename=None):
        """
        The output method that saves the content to a file and renders
        the appropriate template with the file's URL.
        """
        new_filepath = self.get_filepath(content, basename=basename)
        print(new_filepath)
        if not self.storage.exists(new_filepath) or forced:
            self.storage.save(new_filepath, ContentFile(content.encode(self.charset)))
        url = get_static_url(mark_safe(new_filepath))
        return self.render_output(mode, {"url": url})
