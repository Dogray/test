import unittest
from didneywurl import didneywurlstuff

class wurlTest(unittest.TestCase):
    def test_wurl_1(self):
        didney_c = didneywurlstuff()
        test_var = didney_c.testFunc()
        self.assertEqual("Hello wurl!",test_var)