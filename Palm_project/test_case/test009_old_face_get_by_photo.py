from common.myunit import StartEnd
from businessView.face_function import Face
import pytest
import logging


class Test_OldFaceGet(StartEnd):

    @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_get_old_face_by_photo(self):
        logging.info('==========test_get_old_face_by_photo start============')
        l = Face(self.driver)
        assert l.get_old_face() == True

if __name__ == '__main__':
    pytest.main(['-s','test009_old_face_get_by_photo.py'])