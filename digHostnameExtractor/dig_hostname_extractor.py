# -*- coding: utf-8 -*-
# @Author: darkshadows123

import re
from sets import Set

################################################
# Main
################################################

class DIGHostnameExtractor(object):
    """Extractor of md5 hash from text.

    Users of this class should call DIGHostnameExtractor.extract_hostname(), see documentation.
    """

    def extract_hostname(self, string):
        """Extract all hostnames from string.
        :param string: the text to extract from
        """
        pattern = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
        hostnames = re.findall(pattern, string)

        return hostnames


