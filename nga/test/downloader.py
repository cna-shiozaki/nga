import unittest

from nga.downloader.downloader import Downloader 

class DownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.downloader = Downloader()

    def test_remove_unwanted_chars(self):
        title1 = 'Woman of the "Orient"'
        title1_wo_unw_chars = self.downloader.remove_unwanted_chars(title1)

        self.assertEqual(title1_wo_unw_chars, 'Woman of the Orient')

