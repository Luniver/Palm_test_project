from Palm_project.common.desired_caps import appium_desired
from Palm_project.businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time

class Constellation(HomeView):

    constellation_everday = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_constellation"]/android.widget.FrameLayout[1]')
    constellation_match = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_constellation"]/android.widget.FrameLayout[2]')

    subscribe_button = (By.ID, 'com.palm.test:id/btn_pay')

    month_button = (By.ID,'com.palm.test:id/view_payment_btn2')
    year_button = (By.ID,'com.palm.test:id/view_payment_btn1')
    GP_subscribe_button = (By.ID,'com.android.vending:id/footer_placeholder')

    Aries = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[1]')
    Taurus = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[2]')
    Gemini = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[3]')
    Cancer = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[4]')
    Leo = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[5]')
    Virgo = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[6]')
    Libra = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[7]')
    Scorpio = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[8]')
    Sagittarius = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[9]')
    Capricornus = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[10]')
    Aquarius = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[11]')
    Pisces = (By.XPATH,'//*[@resource-id="com.palm.test:id/rv"]/android.widget.FrameLayout[12]')

    def everyday_costellation_enter(self):
        '''每日星座功能进入'''
        self.switch_Constellation()
        logging.info('============select and enter everyday constellation==========')
        try:
            everyday_constellation = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the everyday constellation')
        else:
            everyday_constellation.click()

        time.sleep(4)
        self.getScreenShot('everyday constellation page')


    def constellation_Match_enter(self):
        '''星座匹配界面功能进入'''
        self.switch_Constellation()
        logging.info('========select and enter constellation matching========')
        try:
            constellation_match = self.driver.find_element(*self.constellation_match)
        except NoSuchElementException:
            print('can not find the constellation matching')
        else:
            constellation_match.click()

    def same_constellation_match(self,):
        '''相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Aries match Aries=======')
        try:
            constellation_match = self.driver.find_element(*self.Aries)
        except NoSuchElementException:
            print('can not find the Aries')
        else:
            constellation_match.click()



if __name__ == '__main__':
    driver = appium_desired()
    l = Constellation(driver)
    # l.everyday_costellation_enter()
    l.same_constellation_match()

