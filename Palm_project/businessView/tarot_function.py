from common.desired_caps import appium_desired
from businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time

class Tarot(HomeView):
    tarot_everyday = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_tarot"]/android.widget.FrameLayout[1]')

    tarot1 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[2]')
    tarot2 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[9]')
    tarot3 = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv"]/android.widget.LinearLayout[17]')


    tarot_close = (By.ID,'com.palm.test:id/iv_close')
    share = (By.ID,'com.palm.test:id/iv_titlebar_share')

    def everyday_tarot_enter(self):
        '''每日塔罗牌功能进入'''
        self.switch_tarot()
        logging.info('=======select and enter everyday tarot========')
        try:
            everyday_tarot = self.driver.find_element(*self.tarot_everyday)
        except NoSuchElementException:
            print('can not find the everyday tarot')
            return False
        else:
            everyday_tarot.click()
            self.getScreenShot('TarotEveryday enterPage')
            return True

    def get_three_tarot(self):
        '''塔罗牌的抽取'''
        self.everyday_tarot_enter()


        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        time.sleep(2)
        self.getScreenShot('get first tarot page')


        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        time.sleep(2)
        self.getScreenShot('get second tarot page')


        logging.info('=========start get third tarot==========')
        try:
            third_tarot = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third_tarot.click()
        logging.info('========get third tarot information=========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)
        self.getScreenShot('get all tarot page')
        logging.info('=======get all tarot information')
        return True

    def nothing_tarot_share(self):
        '''没有塔罗牌时点击分享分享'''
        self.everyday_tarot_enter()
        return self.driver.find_element(*self.share).is_enabled()

    def one_tarot_share(self):
        '''有一张塔罗牌时点击分享'''
        self.everyday_tarot_enter()

        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        return self.driver.find_element(*self.share).is_enabled()

    def two_tarot_share(self):
        '''有两张塔罗牌时点击分享'''
        self.everyday_tarot_enter()

        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        return self.driver.find_element(*self.share).is_enabled()

    def three_tarot_share(self):
        '''三张塔罗牌时点击分享'''
        self.everyday_tarot_enter()

        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
            return False
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
            return False
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=========start get third tarot==========')
        try:
            third_tarot = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
            return False
        else:
            third_tarot.click()
        logging.info('========get third tarot information=========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        try:
            share = self.driver.find_element(*self.share)
        except NoSuchElementException:
            print('can not find the share button')
            return False
        else:
            return self.driver.find_element(*self.share).is_enabled()



if __name__ == '__main__':
    driver = appium_desired()
    l = Tarot(driver)
    # l.everyday_tarot_enter()
    # l.get_three_tarot()
    # l.nothing_tarot_share()
    # l.one_tarot_share()
    # l.two_tarot_share()
    l.three_tarot_share()

