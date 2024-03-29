from common.myunit import StartEnd
from businessView.Constellation_function import Constellation
import logging
import pytest

class Test_ConstellationEveryday(StartEnd):

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_constellation_everyday_enter(self):
        logging.info('=========test_constellation_everyday_enter start ======')
        l = Constellation(self.driver)
        assert l.everyday_costellation_enter() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_constellation_everyday_today(self):
        logging.info('=========test_constellation_everyday_today start=========')
        l = Constellation(self.driver)
        assert l.everyday_constellation_today() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_constellation_everyday_tomorrow(self):
        logging.info('========test_constellation_everyday_tomorrow start========')
        l= Constellation(self.driver)
        assert l.everyday_constellation_tomorrow() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_constellation_everyday_future(self):
        logging.info('========test_constellation_everyday_future start=========')
        l = Constellation(self.driver)
        assert l.everyday_constellation_future() ==True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_constellation_everyday_more(self):
        logging.info('=======test_constellation_everyday_more start=======')
        l = Constellation(self.driver)
        assert l.everyday_constellation_more() == True

if __name__ == '__main__':
    pytest.main(['-s','test006_constellation_everyday.py'])