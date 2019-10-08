from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.Constellation_function import Constellation
import unittest
import logging

class ConstellationEveryday(StartEnd):

    def test_constellation_everyday_enter(self):
        logging.info('=========test_constellation_everyday_enter start ======')
        l = Constellation(self.driver)
        self.assertTrue(l.everyday_costellation_enter())

    def test_constellation_everyday_today(self):
        logging.info('=========test_constellation_everyday_today start=========')
        l = Constellation(self.driver)
        self.assertTrue(l.everyday_constellation_today())

    def test_constellation_everyday_tomorrow(self):
        logging.info('========test_constellation_everyday_tomorrow start========')
        l= Constellation(self.driver)
        self.assertTrue(l.everyday_constellation_tomorrow())

    def test_constellation_everyday_future(self):
        logging.info('========test_constellation_everyday_future start=========')
        l = Constellation(self.driver)
        self.assertTrue(l.everyday_constellation_future())

    def test_constellation_everyday_more(self):
        logging.info('=======test_constellation_everyday_more start=======')
        l = Constellation(self.driver)
        self.assertTrue(l.everyday_constellation_more())

if __name__ == '__main__':
    unittest.main()