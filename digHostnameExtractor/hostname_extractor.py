# -*- coding: utf-8 -*-
# @Author: darkshadows123

import copy
from digExtractor.extractor import Extractor
from dig_hostname_extractor import DIGHostnameExtractor


class HostnameExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']
        self.dhostname = DIGHostnameExtractor()

    def extract(self, doc):
        if 'text' in doc:
            return self.dhostname.extract_hostname(doc['text'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields
