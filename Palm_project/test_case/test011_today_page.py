from common.myunit import StartEnd
from businessView.todayview import Today
import pytest
import logging


class Test_Todat_test(StartEnd):

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_today_page_enter(self):
        logging.info('=======test_today_page_enter start=======')
        l = Today(self.driver)
        assert l.today_page_enter() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_today_page_share(self):
        logging.info('=======test_today_page_share start=======')
        l = Today(self.driver)
        assert l.today_page_share() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_today_get_one_tarot(self):
        logging.info('=======test_today_get_one_tarot start=======')
        l = Today(self.driver)
        assert l.today_get_one_tarot() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_today_get_two_tarot(self):
        logging.info('=======test_today_get_two_tarot start=======')
        l = Today(self.driver)
        assert l.today_get_two_tarot() == True

    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_today_get_three_tarot(self):
        logging.info('=======test_today_get_three_tarot start========')
        l = Today(self.driver)
        assert l.today_get_three_tarot() == True

if __name__ == '__main__':
    pytest.main('-s','test011_today_page.py')