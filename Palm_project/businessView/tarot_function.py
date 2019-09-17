from Palm_project.common.desired_caps import appium_desired
from Palm_project.businessView.homeview import HomeView
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

    def everyday_tarot_enter(self):
        '''每日塔罗牌功能进入'''
        self.switch_tarot()
        logging.info('=======select and enter everyday tarot========')
        try:
            everyday_tarot = self.driver.find_element(*self.tarot_everyday)
        except NoSuchElementException:
            print('can not find the everyday tarot')
        else:
            everyday_tarot.click()

    def get_three_tarot(self):
        '''塔罗牌的抽取'''
        self.everyday_tarot_enter()


        logging.info('=======start get first tarot=======')
        try:
            first_tarot = self.driver.find_element(*self.tarot1)
        except NoSuchElementException:
            print('can not find the first tarot')
        else:
            first_tarot.click()
        logging.info('============get first tarot information==========')
        time.sleep(3)
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        time.sleep(2)


        logging.info('=======start get second tarot=========')
        try:
            second_tarot = self.driver.find_element(*self.tarot2)
        except NoSuchElementException:
            print('can not find the second tarot')
        else:
            second_tarot.click()
        logging.info('==========get second tarot information========')
        time.sleep(3)
        WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_close'))).click()
        time.sleep(2)


        logging.info('=========start get third tarot==========')
        try:
            third_tarot = self.driver.find_element(*self.tarot3)
        except NoSuchElementException:
            print('can not find the third tarot')
        else:
            third_tarot.click()
        logging.info('========get third tarot information=========')
        time.sleep(3)
        WebDriverWait(self.driver, 20, 1).until(
            EC.visibility_of_element_located((By.ID, 'com.palm.test:id/iv_close'))).click()
        time.sleep(2)

        logging.info('=======get all tarot information')

if __name__ == '__main__':
    driver = appium_desired()
    l = Tarot(driver)
    # l.everyday_tarot_enter()
    l.get_three_tarot()



