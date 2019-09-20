from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.Constellation_function import Constellation
import unittest
import logging


class Constellation_match(StartEnd):

    # @unittest.skip('test_constellation_Match_enter')
    def test_constellation_Match_enter(self):
        logging.info('==========test constellation_Match_enter start===========')
        l = Constellation(self.driver)
        self.assertTrue(l.constellation_Match_enter())

    # @unittest.skip('test_same_Aries_match')
    def test_same_Aries_match(self):
        logging.info('=========test_same_Aries_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Aries_match())

    # @unittest.skip('test_same_Taurus_match')
    def test_same_Taurus_match(self):
        logging.info('=========test_same_Taurus_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Taurus_match())

    # @unittest.skip('test_same_Gemini_match')
    def test_same_Gemini_match(self):
        logging.info('=========test_same_Gemini_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Gemini_match())

    # @unittest.skip('test_same_Cancer_match')
    def test_same_Cancer_match(self):
        logging.info('=========test_same_Cancer_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Cancer_match())

    # @unittest.skip('test_same_Leo_match')
    def test_same_Leo_match(self):
        logging.info('=========test_same_Leo_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Leo_match())

    # @unittest.skip('test_same_Virgo_match')
    def test_same_Virgo_match(self):
        logging.info('=========test_same_Virgo_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Virgo_match())

    # @unittest.skip('test_same_Gemini_match')
    def test_same_Libra_match(self):
        logging.info('=========test_same_Libra_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Libra_match())

    # @unittest.skip('test_same_Scorpio_match')
    def test_same_Scorpio_match(self):
        logging.info('=========test_same_Scorpio_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Scorpio_match())

    # @unittest.skip('test_same_Sagittarius_match')
    def test_same_Sagittarius_match(self):
        logging.info('=========test_same_Sagittarius_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Sagittarius_match())

    # @unittest.skip('test_same_Capricornus_match')
    def test_same_Capricornus_match(self):
        logging.info('=========test_same_Capricornus_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Capricornus_match())

    # @unittest.skip('test_same_Aquarius_match')
    def test_same_Aquarius_match(self):
        logging.info('=========test_same_Aquarius_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Aquarius_match())

    # @unittest.skip('test_same_Pisces_match')
    def test_same_Pisces_match(self):
        logging.info('=========test_same_Pisces_match start==========')
        l =Constellation(self.driver)
        self.assertTrue(l.same_Pisces_match())


if __name__ == '__main__':
    unittest.main()