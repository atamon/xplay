import unittest

from matcher import match


class TestMatcher(unittest.TestCase):

    def setUp(self):
        self.source = 'Parks S06 E09'

    def testMatchSuccess(self):
        subject = 'Parks.and.Recreation.S06E09.720p.HDTV.X264-DIMENSION.mkv'
        self.assertTrue(match(self.source, subject))

    def testMatchFail(self):
        subject = 'Parks.and.Recreation.S06E05.720p.HDTV.X264-DIMENSION.mkv'
        source = 'Parks 6 9'

        self.assertFalse(match(source, subject))
if __name__ == '__main__':
    unittest.main()
