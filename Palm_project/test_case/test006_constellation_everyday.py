from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.Constellation_function import Constellation
import unittest
import logging

class ConstellationEveryday(StartEnd):

    def test_constellation_everyday_enter(self):
        logging.info('=========test_constellation_everyday_enter start ======')
        l = Constellation(self.driver)
        self.assertTrue(l.everyday_costellation_enter())

if __name__ == '__main__':
    unittest.main()