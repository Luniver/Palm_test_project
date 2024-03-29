from common.myunit import StartEnd
from businessView.face_function import Face
import pytest
import logging

class Test_OldFace(StartEnd):

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_old_face_enter(self):
        logging.info('========test_old_face_enter  start===========')
        l = Face(self.driver)
        assert l.old_face_enter() == True

if __name__ == '__main__':
    pytest.main(['-s','test008_old_face_enter.py'])