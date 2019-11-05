from common.myunit import StartEnd
from businessView.face_function import Face
import unittest
import logging


class OldFaceGet(StartEnd):

    def test_get_old_face_by_photo(self):
        logging.info('==========test_get_old_face_by_photo start============')
        l = Face(self.driver)
        self.assertTrue(l.get_old_face())

if __name__ == '__main__':
    unittest.main()