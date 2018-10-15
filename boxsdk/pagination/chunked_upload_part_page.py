# coding: utf-8

from __future__ import unicode_literals, absolute_import

from .page import Page


class ChunkedUploadPartPage(Page):
    def __getitem__(self, key):
        item_json = self._response_object[self._item_entries_key_name][key]
        item_class = self._translator.translate(item_json['chunked_upload_part'])
        kwargs = {'object_id': item_json['part_id']}

        item = item_class(response_object=item_json, **kwargs)
        return item
