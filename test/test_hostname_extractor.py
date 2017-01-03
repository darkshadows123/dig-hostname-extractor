import unittest

# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from digExtractor.extractor_processor import ExtractorProcessor
from digHostnameExtractor.hostname_extractor import HostnameExtractor

class TestHostnameExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hostname_extractor(self):
        doc = {'text' : 'Hi im Natsume, check out my site brun1989.itldc-customer.net and https://www.google.com'}

        extractor = HostnameExtractor().set_metadata({'extractor': 'ipaddress'})
        ep = ExtractorProcessor().set_input_fields(['text'])\
                                 .set_output_field('extracted')\
                                 .set_extractor(extractor)
        updated_doc = ep.extract(doc)
        result = updated_doc['extracted'][0]['result']
        self.assertEqual(result[0]['value'],
                         'brun1989.itldc-customer.net')
        self.assertEqual(result[1]['value'],
                         'www.google.com')

if __name__ == '__main__':
    unittest.main()
