from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.loginview import Loginview
import unittest
import logging

class Information_Input(StartEnd):

    # @unittest.skip('test_information_english')
    def test_information_english(self):
        logging.info('=====test_username_input_english======')
        l = Loginview(self.driver)
        username = "lichenyu"
        self.assertTrue(l.username_input(username))
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())

    def test_information_chinese(self):
        logging.info('=====test_username_input_chinese======')
        l = Loginview(self.driver)
        username = "李宸宇"
        self.assertTrue(l.username_input(username))
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())

    def test_information_japanese(self):
        logging.info('=====test_username_input_japanese======')
        l = Loginview(self.driver)
        username = "本当ですか"
        self.assertTrue(l.username_input(username))
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())

    def test_information_french(self):
        logging.info('=====test_username_input_french======')
        l = Loginview(self.driver)
        username = "Vraiment?"
        self.assertTrue(l.username_input(username))
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())

    def test_information_korean(self):
        logging.info('=====test_username_input_korean======')
        l = Loginview(self.driver)
        username = "진짜예요?"
        self.assertTrue(l.username_input(username))
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())

    # @unittest.skip('test_information_birthday_select')
    def test_information_birthday_select(self):
        logging.info('======test_birthday_select=======')
        l = Loginview(self.driver)
        self.assertTrue(l.birthday_select())
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())

    # @unittest.skip('test_information_sex_select')
    def test_information_sex_select(self):
        logging.info('=======test_sex_select=========')
        l = Loginview(self.driver)
        # self.assertTrue(l.female_select())
        self.assertTrue(l.male_select())
        self.assertFalse(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled())




if __name__ == '__main__':
    unittest.main()