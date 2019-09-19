from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.palm_function import Palm
import unittest
import logging

class Palm_judge(StartEnd):

    def test_palm_judge_enter(self):
        logging.info("==========test_palm_judge_enter start ==========")
        l = Palm(self.driver)
        self.assertTrue(l.palm_judgement_enter())

    def test_palm_judge_lifeline(self):
        logging.info("==========test_palm_judge_lifeline start ==========")
        l = Palm(self.driver)
        self.assertTrue(l.palm_judge_lifeline())

    def test_palm_judge_heartline(self):
        logging.info("==========test_palm_judge_heartline start ==========")
        l = Palm(self.driver)
        self.assertTrue(l.palm_judge_heartline())

    def test_palm_judge_businessline(self):
        logging.info("==========test_palm_judge_businessline start ==========")
        l = Palm(self.driver)
        self.assertTrue(l.palm_judge_businessline())

    def test_palm_judge_headline(self):
        logging.info("==========test_palm_judge_headline start ==========")
        l = Palm(self.driver)
        self.assertTrue(l.palm_judge_headline())

    def test_palm_judge_destinyline(self):
        logging.info("==========test_palm_judge_destinyline start ==========")
        l = Palm(self.driver)
        self.assertTrue(l.palm_judge_destinyline())

if __name__ == '__main__':
    unittest.main()



