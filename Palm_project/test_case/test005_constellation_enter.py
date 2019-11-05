from common.myunit import StartEnd
from businessView.Constellation_function import Constellation
import unittest
import logging

class ConstellationPage_enter(StartEnd):

    #@unittest.skip('test_constellationPage_enter')
    def test_constellationPage_enter(self):
        logging.info('=======test_constellationPage_enter start=======')
        l = Constellation(self.driver)
        self.assertTrue(l.switch_Constellation())

if __name__ == '__main__':
    unittest.main()


