from common.myunit import StartEnd
from businessView.psychological_test_function import Psychological
import unittest
import logging

class Psychological_test(StartEnd):

    def test_question_1_enter(self):
        logging.info('===========test_question_1_enter start===========')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_1())

    def test_question_2_enter(self):
        logging.info('===========test_question_2_enter start============')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_2())

    def test_question_1_answer_yes(self):
        '''问题1全部回答yes'''
        logging.info('============test_question_1_answer_yes start==========')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_all_yes_1())

    def test_question_1_answer_no(self):
        '''问题1全部回答no'''
        logging.info('============test_question_1_answer_no start===========')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_all_no_1())

    def test_question_1_quit_yes(self):
        '''问题1中途退出点击yes'''
        logging.info('============test_question_1_quit_yes start=============')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_1_quit_yes())

    def test_question_1_quit_no(self):
        '''问题1中途退出点击no'''
        logging.info('============test_question_1_quit_no start==============')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_1_quit_no())

    def test_question_2_answer_yes(self):
        '''问题2全部回答yes'''
        logging.info('============test_question_2_answer_yes start==========')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_all_yes_2())

    def test_question_2_answer_no(self):
        '''问题2全部回答no'''
        logging.info('============test_question_2_answer_no start===========')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_all_no_2())

    def test_question_2_quit_yes(self):
        '''问题2中途退出点击yes'''
        logging.info('============test_question_2_quit_yes start=============')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_2_quit_yes())

    def test_question_2_quit_no(self):
        '''问题2中途退出点击no'''
        logging.info('============test_question_2_quit_no start==============')
        l = Psychological(self.driver)
        self.assertTrue(l.psychological_question_2_quit_no())


if __name__ == '__main__':
    unittest.main()