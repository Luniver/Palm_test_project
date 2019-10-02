from Palm_project.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from Palm_project.businessView.loginview import Loginview
import logging,time
from selenium.webdriver.common.by import By

class HomeView(Loginview):

    item_image = (By.ID,'com.palm.test:id/rl_bg')
    navigation_home = (By.XPATH,'//*[@resource-id="com.palm.test:id/navigation_home"]/android.widget.ImageView[1]')
    navigation_today = (By.XPATH,'//*[@resource-id="com.palm.test:id/navigation_today"]/android.widget.ImageView[1]')
    navigation_me = (By.XPATH,'//*[@resource-id="com.palm.test:id/navigation_me"]/android.widget.ImageView[1]')
    closeBtn = (By.ID, 'com.palm.test:id/iv_payment_close')

    def switch_navigation_home(self):
        '''切换至首页'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('========switch to navigation_home=========')
            try:
                home = self.driver.find_element(*self.navigation_home)
            except NoSuchElementException:
                print('can not find navigation_home')
                return False
            else:
                home.click()
            time.sleep(2)
            self.getScreenShot('navigation_home')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_element(*self.navigation_home).click()
            return True

    def switch_navigation_today(self):
        '''切换至今日'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('========switch to navigation_today========')
            try:
                today = self.driver.find_element(*self.navigation_today)
            except NoSuchElementException:
                print('can not find navigation_today')
                return False
            else:
                today.click()
            time.sleep(2)
            self.getScreenShot('navigation today')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_element(*self.navigation_today).click()
            return True

    def switch_navigation_me(self):
        '''切换到我的'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('=======switch to navigation_me===========')
            try:
                me = self.driver.find_element(*self.navigation_me)
            except NoSuchElementException:
                print('can not find navigation_me')
                return False
            else:
                me.click()
            time.sleep(2)
            self.getScreenShot('navigation_me')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_element(*self.navigation_me).click()
            return True



    def switch_palm(self):
        '''切换到手相功能页'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('=======switch to palm page=========')
            try:
                palm = self.driver.find_elements(*self.item_image)[0]
            except NoSuchElementException:
                print('can not find palm page')
                return False
            else:
                palm.click()
            time.sleep(2)
            self.getScreenShot('palm_home')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_elements(*self.item_image)[0].click()
            return True

    def switch_Constellation(self):
        '''切换到星座功能页'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            time.sleep(2)
            logging.info('=======switch to Constellation page=========')
            try:
                horoscope = self.driver.find_elements(*self.item_image)[1]
            except NoSuchElementException:
                print('can not find Constellation page')
                return False
            else:
                horoscope.click()
                time.sleep(2)
                self.getScreenShot('Constellation_home')
                return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_elements(*self.item_image)[1].click()
            return True

    def switch_tarot(self):
        '''切换到塔罗牌功能页'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('=======switch to tarot page=========')
            try:
                tarot = self.driver.find_elements(*self.item_image)[2]
            except NoSuchElementException:
                print('can not find tarot page')
                return False
            else:
                tarot.click()
            time.sleep(2)
            self.getScreenShot('tarot_home')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_elements(*self.item_image)[2].click()
            return True

    def switch_face(self):
        '''切换到变老功能页'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('=======switch to face page=========')
            try:
                face = self.driver.find_elements(*self.item_image)[3]
            except NoSuchElementException:
                print('can not find face page')
                return False
            else:
                face.click()
            time.sleep(2)
            self.getScreenShot('face_home')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_elements(*self.item_image)[3].click()
            return True

    def switch_psychological_test(self):
        '''切换至心理测试功能页'''
        time.sleep(2)
        try:
            dingyuePage = self.driver.find_element(*self.closeBtn)
        except NoSuchElementException:
            logging.info('=========plan A enter========')
            self.username_input('lichenyu')
            self.birthday_select()
            self.male_select()
            self.next_button()
            self.allow_event()
            self.back_event()
            self.close_event()
            logging.info('=======switch to psychological_test page=========')
            try:
                psychological_test = self.driver.find_elements(*self.item_image)[4]
            except NoSuchElementException:
                print('can not find psychological_test page')
                return False
            else:
                psychological_test.click()
            time.sleep(2)
            self.getScreenShot('psychological_test_home')
            return True
        else:
            logging.info('========plan B enter=======')
            dingyuePage.click()
            self.driver.find_elements(*self.item_image)[4].click()
            return True



if __name__ == '__main__':
    driver = appium_desired()
    l = HomeView(driver)
    # l.switch_navigation_home()
    # l.switch_navigation_today()
    # l.switch_navigation_me()
    # l.switch_palm()
    # l.switch_Constellation()
    # l.switch_tarot()
    # l.switch_face()
    l.switch_psychological_test()






