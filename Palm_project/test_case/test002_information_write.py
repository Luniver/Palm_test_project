from common.myunit import StartEnd
from businessView.loginview import Loginview
import unittest
import logging
import pytest

class Test_Information_Input(StartEnd):

    @pytest.skip('test_information_english')
    def test_information_english(self):
        logging.info('=====test_username_input_english start ======')
        l = Loginview(self.driver)
        username = "lichenyu"
        assert(l.username_input(username)) == "lichenyu"
        assert(self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled()) == True

    @pytest.skip('test_information_chinese')
    def test_information_chinese(self):
        logging.info('=====test_username_input_chinese start ======')
        l = Loginview(self.driver)
        username = "李宸宇"
        assert l.username_input(username) == "李宸宇"
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() ==True

    @pytest.skip('test_information_japanese')
    def test_information_japanese(self):
        logging.info('=====test_username_input_japanese start ======')
        l = Loginview(self.driver)
        username = "本当ですか"
        assert l.username_input(username) == "本当ですか"
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() == True

    @pytest.skip('test_information_french')
    def test_information_french(self):
        logging.info('=====test_username_input_french start ======')
        l = Loginview(self.driver)
        username = "Vraiment?"
        assert (l.username_input(username)) == "Vraiment?"
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() == True

    @pytest.skip('test_information_korean')
    def test_information_korean(self):
        logging.info('=====test_username_input_korean start ======')
        l = Loginview(self.driver)
        username = "진짜예요?"
        assert l.username_input(username) == "진짜예요?"
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() == True

    @pytest.skip('test_information_spain')
    def test_information_spain(self):
        logging.info('=====test_username_input_spain start ======')
        l = Loginview(self.driver)
        username = "Nombre de usuario"
        assert l.username_input(username) == "Nombre de usuario"
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() == True
    @pytest.skip('test_information_birthday_select')
    def test_information_birthday_select(self):
        logging.info('======test_birthday_select start =======')
        l = Loginview(self.driver)
        assert l.birthday_select() ==True
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() == False

    @pytest.skip('test_information_sex_select')
    def test_information_sex_select(self):
        logging.info('=======test_sex_select start =========')
        l = Loginview(self.driver)
        # self.assertTrue(l.female_select())
        assert l.male_select() == True
        assert self.driver.find_element_by_id('com.palm.test:id/tv_app_next').is_enabled() == False




if __name__ == '__main__':
    pytest.main(['-s','test002_information_write.py'])