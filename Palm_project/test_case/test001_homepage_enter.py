from Palm_project.common.myunit import StartEnd
from Palm_project.businessView.homeview import HomeView
import unittest
import pytest
import logging


class Home_enter(StartEnd):

    # @unittest.skip('test_home_enter')
    # @pytest.fixture()
    def test_home_enter(self):
        logging.info('test_information_finish')
        # username = '李宸宇'
        l = HomeView(self.driver)
        # self.assertTrue(l.username_input(username))
        # self.assertTrue(l.birthday_select())
        # # self.assertTrue(l.male_select())
        # self.assertTrue(l.female_select())
        # self.assertTrue(l.next_button())
        # l.allow_event()
        # self.assertTrue(l.back_event())
        self.assertTrue(l.switch_navigation_home())

if __name__ == '__main__':
    unittest.main()
