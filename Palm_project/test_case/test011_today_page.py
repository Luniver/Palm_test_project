from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.todayview import Today
import unittest
import logging


class Todat_test(StartEnd):

    def test_today_page_enter(self):
        logging.info('=======test_today_page_enter start=======')
        l = Today(self.driver)
        self.assertTrue(l.today_page_enter())

    def test_today_page_share(self):
        logging.info('=======test_today_page_share start=======')
        l = Today(self.driver)
        self.assertTrue(l.today_page_share())

    def test_today_get_one_tarot(self):
        logging.info('=======test_today_get_one_tarot start=======')
        l = Today(self.driver)
        self.assertTrue(l.today_get_one_tarot())

    def test_today_get_two_tarot(self):
        logging.info('=======test_today_get_two_tarot start=======')
        l = Today(self.driver)
        self.assertTrue(l.today_get_two_tarot())

    def test_today_get_three_tarot(self):
        logging.info('=======test_today_get_three_tarot start========')
        l = Today(self.driver)
        self.assertTrue(l.today_get_three_tarot())

if __name__ == '__main__':
    unittest.main()