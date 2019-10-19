from Palm_project.common.desired_caps import appium_desired
from Palm_project.businessView.homeview import HomeView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging,time,os

class Face(HomeView):

    old_face = (By.CLASS_NAME,'android.widget.FrameLayout')
    face_takephoto =(By.ID,'com.palm.test:id/face_picture')
    face_picture = (By.ID,'com.palm.test:id/face_picture_choose')
    picture = (By.CLASS_NAME,'android.widget.FrameLayout')
    face_ok = (By.ID,'com.palm.test:id/face_ok')

    PermissionYes = (By.ID,'com.palm.test:id/tv_positive')
    PermissionNo = (By.ID,'com.palm.test:id/tv_negative')
    PrivacyPolicy = (By.ID,'com.palm.test:id/tv_policy')

    def old_face_enter(self):
        '''变老功能的进入'''
        self.switch_face()
        logging.info('========select and enter old face========')
        try:
            face = self.driver.find_elements(*self.old_face)[1]
        except NoSuchElementException:
            print('can not find the old face button')
            return False
        else:
            face.click()
            self.getScreenShot('Face_homepage')
            return True

    def get_old_face(self):
        '''变老拍照'''
        self.old_face_enter()
        self.allow_event()
        logging.info('========into picture======')
        try:
            picture = self.driver.find_element(*self.face_picture)
        except NoSuchElementException:
            print('can not find the face picture')
            return False
        else:
            picture.click()
        self.allow_event()
        time.sleep(2)
        logging.info('=======choose a picture=======')
        os.system('adb shell input tap 395 357')
        time.sleep(2)

        logging.info('=======picture sure=========')
        try:
            picture_ok = self.driver.find_element(*self.face_ok)
        except NoSuchElementException:
            print('can not find the ok button')
            return False
        else:
            picture_ok.click()

        logging.info('=======Permission Need=========')
        try:
            Yes = self.driver.find_element(*self.PermissionYes)
        except NoSuchElementException:
            print('can not find the PermissionYes')
            return False
        else:
            Yes.click()

        time.sleep(2)


        logging.info('=======wait the old face result=======')
        # WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located((By.ID,'com.palm.test:id/iv_payment_close'))).clcik()
        self.close_event()
        time.sleep(2)
        self.getScreenShot('old face result')
        return True

if __name__ == '__main__':
    driver = appium_desired()
    l = Face(driver)
    # l.old_face_enter()
    l.get_old_face()



