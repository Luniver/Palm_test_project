from Palm_project.common.desired_caps import appium_desired
from Palm_project.businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time


class Psychological(HomeView):

    psychological_1 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[1]')
    psychological_2 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[2]')
    psychological_3 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[3]')
    psychological_4 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[4]')
    psychological_5 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[5]')
    psychological_6 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[6]')
    psychological_7 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[7]')
    psychological_8 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_psychology"]/android.widget.FrameLayout[8]')


    def psychological_question_1(self):
        '''心理测试问题1的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 1 enter')
        try:
            psychological_1 = self.driver.find_element(*self.psychological_1)
        except NoSuchElementException:
            print('can not find the psychological question 1')
        else:
            psychological_1.click()

    def psychological_question_2(self):
        '''心理测试问题2的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 2 enter')
        try:
            psychological_2 = self.driver.find_element(*self.psychological_2)
        except NoSuchElementException:
            print('can not find the psychological question 2')
        else:
            psychological_2.click()


    def psychological_question_3(self):
        '''心理测试问题3的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 3 enter')
        try:
            psychological_3 = self.driver.find_element(*self.psychological_3)
        except NoSuchElementException:
            print('can not find the psychological question 3')
        else:
            psychological_3.click()


    def psychological_question_4(self):
        '''心理测试问题4的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 4 enter')
        try:
            psychological_4 = self.driver.find_element(*self.psychological_4)
        except NoSuchElementException:
            print('can not find the psychological question 4')
        else:
            psychological_4.click()


    def psychological_question_5(self):
        '''心理测试问题5的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 5 enter')
        try:
            psychological_5 = self.driver.find_element(*self.psychological_5)
        except NoSuchElementException:
            print('can not find the psychological question 5')
        else:
            psychological_5.click()


    def psychological_question_6(self):
        '''心理测试问题6的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 6 enter')
        try:
            psychological_6 = self.driver.find_element(*self.psychological_6)
        except NoSuchElementException:
            print('can not find the psychological question 6')
        else:
            psychological_6.click()


    def psychological_question_7(self):
        '''心理测试问题7的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 7 enter')
        try:
            psychological_7 = self.driver.find_element(*self.psychological_7)
        except NoSuchElementException:
            print('can not find the psychological question 7')
        else:
            psychological_7.click()


    def psychological_question_8(self):
        '''心理测试问题8的进入'''
        self.switch_psychological_test()
        logging.info('psychological question 8 enter')
        try:
            psychological_8 = self.driver.find_element(*self.psychological_8)
        except NoSuchElementException:
            print('can not find the psychological question 8')
        else:
            psychological_8.click()

if __name__ == '__main__':
    driver = appium_desired()
    l = Psychological(driver)
    l.psychological_question_1()
