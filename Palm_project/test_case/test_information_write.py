from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.loginview import Loginview
import unittest
import logging

class Information_Input(StartEnd):

    # @unittest.skip('test_information_username')
    def test_information_username(self):
        logging.info('=====test_username_input======')
        l = Loginview(self.driver)
        username = "lichenyu"
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

    def test_information_finish(self):
        logging.info('test_information_finish')
        username = '李宸宇'
        l = Loginview(self.driver)
        self.assertTrue(l.username_input(username))
        self.assertTrue(l.birthday_select())
        # self.assertTrue(l.male_select())
        self.assertTrue(l.female_select())
        self.assertTrue(l.next_button())


if __name__ == '__main__':
    unittest.main()