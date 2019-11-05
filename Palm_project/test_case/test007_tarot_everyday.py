from common.myunit import StartEnd
from businessView.tarot_function import Tarot
import unittest
import logging


class TarotEveryday(StartEnd):

    def test_tarot_everyday_enter(self):
        logging.info('===========test_tarot_everyday_enter start=========')
        l = Tarot(self.driver)
        self.assertTrue(l.everyday_tarot_enter())

    def test_get_three_tarot(self):
        logging.info('==========test_get_three_tarot start=========')
        l = Tarot(self.driver)
        self.assertTrue(l.get_three_tarot())

    def test_no_tarot_share(self):
        logging.info('==========test_no_tarot_share start===========')
        l = Tarot(self.driver)
        self.assertFalse(l.nothing_tarot_share())

    def test_one_tarot_share(self):
        logging.info('==========test_one_tarot_share start=========')
        l = Tarot(self.driver)
        self.assertFalse(l.one_tarot_share())

    def test_two_tarot_share(self):
        logging.info('===========test_two_tarot_share start==========')
        l = Tarot(self.driver)
        self.assertFalse(l.two_tarot_share())

    def test_three_tarot_share(self):
        logging.info('============test_three_tarot_share start===========')
        l = Tarot(self.driver)
        self.assertTrue(l.three_tarot_share())

if __name__ == '__main__':
    unittest.main()