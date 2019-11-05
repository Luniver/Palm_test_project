from common.myunit import StartEnd
from businessView.face_function import Face
import unittest
import logging

class OldFace(StartEnd):

    def test_old_face_enter(self):
        logging.info('========test_old_face_enter  start===========')
        l = Face(self.driver)
        self.assertTrue(l.old_face_enter())

if __name__ == '__main__':
    unittest.main()