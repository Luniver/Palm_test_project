from Palm_project.common.desired_caps import appium_desired
from Palm_project.businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging,time,os

class Face(HomeView):

    old_face = (By.XPATH,'//*[@resource-id="com.palm.test:id/rcv_face"]/android.widget.FrameLayout[1]')
    face_takephoto =(By.ID,'com.palm.test:id/face_picture')
    face_picture = (By.ID,'com.palm.test:id/face_picture_choose')
    picture = (By.CLASS_NAME,'android.widget.FrameLayout')
    face_ok = (By.ID,'com.palm.test:id/face_ok')

    def old_face_enter(self):
        '''变老功能的进入'''
        self.switch_face()
        logging.info('========select and enter old face========')
        try:
            old_face = self.driver.find_element(*self.old_face)
        except NoSuchElementException:
            print('can not find the old face button')
        else:
            old_face.click()

    def get_old_face(self):
        '''变老拍照'''
        self.old_face_enter()
        logging.info('========into picture======')
        try:
            picture = self.driver.find_element(*self.face_picture)
        except NoSuchElementException:
            print('can not find the face picture')
        else:
            picture.click()

        logging.info('=======choose a picture=======')
        os.system('adb shell input tap 395 357')
        time.sleep(2)

        logging.info('=======picture sure=========')
        try:
            picture_ok = self.driver.find_element(*self.face_ok)
        except NoSuchElementException:
            print('can not find the ok button')
        else:
            picture_ok.click()

        time.sleep(2)


        logging.info('=======wait the old face result=======')
        # WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_payment_close'))).clcik()
        self.close_event()
        time.sleep(2)
        self.getScreenShot('old face result')

if __name__ == '__main__':
    driver = appium_desired()
    l = Face(driver)
    l.get_old_face()



