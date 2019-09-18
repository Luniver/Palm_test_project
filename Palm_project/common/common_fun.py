from Palm_project.baseView.baseView import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging
import time,os,re


class Commom(BaseView):
    cancelBtn = (By.ID,'com.android.systemui:id/back')
    homeBtn = (By.ID,'com.android.systemui:id/home')
    recentBtn = (By.ID,'com.android.systemui:id/recent_apps')

    allow = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    deny = (By.ID, 'com.android.packageinstaller:id/permission_deny_button')

    backBtn = (By.ID, 'com.palm.test:id/iv_palmscan_back')
    closeBtn = (By.ID, 'com.palm.test:id/iv_payment_close')



    def check_cancel_Btn(self):
        logging.info('===========check cancel_btn===========')
        time.sleep(2)
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def allow_event(self):
        '''允许进入'''
        logging.info('========allow to in=============')
        try:
            allowBtn= self.driver.find_element(*self.allow)
        except NoSuchElementException:
            print('can not find the button')
        else:
            allowBtn.click()
        try:
            allowBtn= self.driver.find_element(*self.allow)
        except NoSuchElementException:
            print('can not find the allow toast')
        else:
            allowBtn.click()


    def back_event(self):
        '''返回事件'''
        logging.info('========back event============')
        time.sleep(2)
        try:
            backBtn = self.driver.find_element(*self.backBtn)
        except NoSuchElementException:
            print('can not find the back button')
            return False
        else:
            backBtn.click()
            return True

    def close_event(self):
        '''关闭订阅页'''
        logging.info('========close subscribe page======')
        time.sleep(5)
        try:
            closeBtn = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            print('can not find the close button')
            return False
        else:
            closeBtn.click()
            return True

    def get_page_title(self):
        '''获取页面事件'''
        self.page = self.driver.page_source
        self.titles = re.findall(r'target="_blank">(.*?)</a></h2>', self.page)
        for title in self.titles:
            print(title)
