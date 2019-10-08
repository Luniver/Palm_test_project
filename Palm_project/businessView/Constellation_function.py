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

    result_title = (By.ID,'com.palm.test:id/tv_titlebar_title')
    everyday_result_title = (By.ID,'com.palm.test:id/iv_cntdaily_cnt')

    today = (By.ID,'com.palm.test:id/tv_cntdaily_today')
    tomorrow = (By.ID,'com.palm.test:id/tv_cntdaily_tomorrow')
    future = (By.ID,'com.palm.test:id/tv_cntdaily_future')
    more = (By.ID,'com.palm.test:id/tv_cntdaily_more')

    def everyday_costellation_enter(self):
        '''每日星座功能进入'''
        self.switch_Constellation()
        logging.info('============select and enter everyday constellation==========')
        try:
            everyday_constellation = self.driver.find_element(*self.constellation_everday)
        except NoSuchElementException:
            print('can not find the everyday constellation')
            return False
        else:
            everyday_constellation.click()
            time.sleep(4)
            try:
                self.driver.find_element(*self.everyday_result_title)
            except NoSuchElementException:
                print('can not get the result page')
                return False
            else:
                self.getScreenShot('everyday constellation page')
                return True

    def everyday_constellation_today(self):
        '''每日星座今日界面'''
        self.everyday_costellation_enter()
        logging.info('===========enter everyday constellation today page===========')
        try:
            today = self.driver.find_element(*self.today)
        except NoSuchElementException:
            print('can not find the today')
            return False
        else:
            today.click()
            time.sleep(2)
            self.getScreenShot('constellation today page')
            return True

    def everyday_constellation_tomorrow(self):
        '''每日星座明日界面'''
        self.everyday_costellation_enter()
        logging.info('=========enter everyday constellation tomorrow page=========')
        try:
            tomorrow = self.driver.find_element(*self.tomorrow)
        except NoSuchElementException:
            print('can not find the tomorrow')
            return False
        else:
            tomorrow.click()
            time.sleep(2)
            self.getScreenShot('constellation tomorrow page')
            return True

    def everyday_constellation_future(self):
        '''每日星座未来界面'''
        self.everyday_costellation_enter()
        logging.info('==========enter everyday constellation future page==========')
        try:
            future = self.driver.find_element(*self.future)
        except NoSuchElementException:
            print('can not find the future')
            return False
        else:
            future.click()
            time.sleep(2)
            self.getScreenShot('constellation future page')
            return True

    def everyday_constellation_more(self):
        '''每日星座更多'''
        self.everyday_costellation_enter()
        logging.info('==========enter everyday constellation more page========')
        try:
            more = self.driver.find_element(*self.more)
        except NoSuchElementException:
            print('can not find the more')
            return False
        else:
            more.click()
            time.sleep(2)
            self.getScreenShot('constellation select page')
            return True


    def constellation_Match_enter(self):
        '''星座匹配界面功能进入'''
        self.switch_Constellation()
        logging.info('========select and enter constellation matching========')
        try:
            constellation_match = self.driver.find_element(*self.constellation_match)
        except NoSuchElementException:
            print('can not find the constellation matching')
            return False
        else:
            constellation_match.click()
            return True

    def same_Aries_match(self):
        '''白羊相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Aries match Aries=======')
        try:
            Aries_match = self.driver.find_element(*self.Aries)
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            Aries_match.click()
            Aries_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Aries constellation match result')
                return True

    def same_Taurus_match(self):
        '''金牛相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Taurus match Taurus=======')
        try:
            Taurus_match = self.driver.find_element(*self.Taurus)
        except NoSuchElementException:
            print('can not find the Taurus')
            return False
        else:
            Taurus_match.click()
            Taurus_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Taurus constellation match result')
                return True

    def same_Gemini_match(self):
        '''双子相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Gemini match Gemini=======')
        try:
            Gemini_match = self.driver.find_element(*self.Gemini)
        except NoSuchElementException:
            print('can not find the Gemini')
            return False
        else:
            Gemini_match.click()
            Gemini_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Gemini constallation match result')
                return True

    def same_Cancer_match(self):
        '''巨蟹相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Cancer match Cancer=======')
        try:
            Cancer_match = self.driver.find_element(*self.Cancer)
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            Cancer_match.click()
            Cancer_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Cancer constellation match result')
                return True

    def same_Leo_match(self):
        '''狮子相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Leo match Leo=======')
        try:
            Leo_match = self.driver.find_element(*self.Leo)
        except NoSuchElementException:
            print('can not find the Leo')
            return False
        else:
            Leo_match.click()
            Leo_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Leo constellation match result')
                return True

    def same_Virgo_match(self):
        '''处女相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Virgo match Virgo=======')
        try:
            Virgo_match = self.driver.find_element(*self.Virgo)
        except NoSuchElementException:
            print('can not find the Virgo')
            return False
        else:
            Virgo_match.click()#点击取消星座引导页面动画
            Virgo_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Virgo constellation match result')
                return True

    def same_Libra_match(self):
        '''天秤相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Libra match Libra=======')
        try:
            Libra_match = self.driver.find_element(*self.Libra)
        except NoSuchElementException:
            print('can not find the Libra')
            return False
        else:
            Libra_match.click()
            Libra_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Libra constellation match result')
                return True

    def same_Scorpio_match(self):
        '''天蝎相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Scorpio match Scorpio=======')
        try:
            Scorpio_match = self.driver.find_element(*self.Scorpio)
        except NoSuchElementException:
            print('can not find the Scorpio')
            return False
        else:
            Scorpio_match.click()
            Scorpio_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Scorpoio constellation match result')
                return True

    def same_Sagittarius_match(self):
        '''射手相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Sagittarius match Sagittarius=======')
        try:
            Sagittarius_match = self.driver.find_element(*self.Sagittarius)
        except NoSuchElementException:
            print('can not find the Sagittarius')
            return False
        else:
            Sagittarius_match.click()
            Sagittarius_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Sagittarius constellation match result')
                return True

    def same_Capricornus_match(self):
        '''摩羯相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Capricornus match Capricornus=======')
        try:
            Capricornus_match = self.driver.find_element(*self.Capricornus)
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            Capricornus_match.click()
            Capricornus_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Capricornus constellation match result')
                return True

    def same_Aquarius_match(self):
        '''水瓶相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Aquarius match Aquarius=======')
        try:
            Aquarius_match = self.driver.find_element(*self.Aquarius)
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            Aquarius_match.click()
            Aquarius_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Aquarius constellation match result')
                return True

    def same_Pisces_match(self):
        '''双鱼相同星座匹配'''
        self.constellation_Match_enter()
        logging.info('=======start Pisces match Pisces=======')
        try:
            Pisces_match = self.driver.find_element(*self.Pisces)
        except NoSuchElementException:
            print('can not find the Aries')
            return False
        else:
            Pisces_match.click()
            Pisces_match.click()
            self.close_event()
            logging.info('=========get constellation match result========')
            try:
                self.driver.find_element(*self.result_title)
            except NoSuchElementException:
                print('can not find the result title')
                return False
            else:
                # print('get constellation match result')
                self.getScreenShot('get Pisces constellation match result')
                return True




if __name__ == '__main__':
    driver = appium_desired()
    l = Constellation(driver)
    # l.everyday_costellation_enter()
    l.same_Sagittarius_match()


