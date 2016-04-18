#-*- coding: UTF-8 -*-
import os
import time
import unittest
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
global driver
fd = open(  'bugReport.txt', 'w')
"""if not os.path.isdir("C:\\Users\\Administrator\\Desktop" ):
	os.mkdir("C:\\Users\\Administrator\\Desktop" )
"""
#目前写的我本地路径，搭建到新的服务器后，文件路径需要修改

class MPTest(unittest.TestCase):

    def setUp(self):
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='4.4.2'
        desired_caps['deviceName']='HUAWEI H60-L01'

        #desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
        #被测试的App在电脑上的位置
        desired_caps['appPackage']='com.yixia.videoeditor'
        desired_caps['appActivity']='.ui.login.SplashActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def test_01login_phone(self):
        #登录测试
        time.sleep(8)
        bt_tiaoguo = self.driver.find_element_by_id("com.yixia.videoeditor:id/titleRightTextView")
        bt_tiaoguo.click()
        time.sleep(8)
        fd.write( "跳过兴趣选择\n")
        time.sleep(5)
        
        bt_shoot_plus =self.driver.find_element_by_id("com.yixia.videoeditor:id/bottom_record")
        bt_shoot_plus.click()
        fd.write( "点击+按钮成功\n")
        time.sleep(5)

        bt_phonelogin =self.driver.find_element_by_id("com.yixia.videoeditor:id/login_phone_button")
        bt_phonelogin.click()
        fd.write( "点击手机号登录按钮成功\n")
        time.sleep(5)
        
        phone_text_login = self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview')
        phone_text_login.click()
        fd.write( "定位手机号输入框成功\n")
        time.sleep(3)
        phone_text_login.send_keys('18610841209')
        fd.write( "输入手机号成功\n")
        time.sleep(3)
        psd = self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview')
        psd.click()
        fd.write( "定位密码输入框成功\n")
        psd.send_keys('123456')
        fd.write( "输入密码成功\n")
        time.sleep(2)

        bt_login = self.driver.find_element_by_id("com.yixia.videoeditor:id/login_button")
        bt_login.click()
        time.sleep(8)
        fd.write( "登录成功\n")
    
    def test_02shoot(self):
        #录制视频并编辑上传
        time.sleep(5)
        shoot_plus =self.driver.find_element_by_id("com.yixia.videoeditor:id/bottom_record")
        shoot_plus.click()
        fd.write( "点击+按钮成功\n")
        time.sleep(5)
        bt_video_camera = self.driver.find_element_by_id("com.yixia.videoeditor:id/video_camera_img")
        bt_video_camera.click()
        time.sleep(3)
        fd.write( "点击拍摄按钮成功\n")
        bt_dyshexiangtou = self.driver.find_element_by_id("com.huawei.systemmanager:id/btn_allow")
        bt_dyshexiangtou.click()
        time.sleep(3)
        fd.write( "允许调用摄像头\n")
        bt_dyhuatong = self.driver.find_element_by_id("com.huawei.systemmanager:id/btn_allow")
        bt_dyhuatong.click()
        time.sleep(3)
        fd.write( "允许调用话筒\n")
        bt_shoot = self.driver.find_element_by_id("com.yixia.videoeditor:id/record_controller")
        bt_shoot.click()
        time.sleep(10)
        fd.write( "开始录制\n")
        bt_shoot = self.driver.find_element_by_id("com.yixia.videoeditor:id/record_controller")
        bt_shoot.click()
        time.sleep(10)
        fd.write( "录制结束\n")
        bt_title_next = self.driver.find_element_by_id("com.yixia.videoeditor:id/title_next")
        bt_title_next.click()
        time.sleep(5)
        fd.write( "点击对勾,进入预览界面\n")

        time.sleep(10)
        bt_title_Right = self.driver.find_element_by_id("com.yixia.videoeditor:id/titleRight")
        bt_title_Right.click()
        time.sleep(20)
        fd.write( "预览结束,进入发布面板\n")

        bt_shareVideo = self.driver.find_element_by_id("com.yixia.videoeditor:id/share_video")
        bt_shareVideo.click()
        time.sleep(15)
        fd.write( "发布按钮点击成功\n")
        bt_shareClose = self.driver.find_element_by_id("com.yixia.videoeditor:id/upload_suc_dialog_close")
        #self.assertIsNotNone(bt_shareClose)
        self.assertIsNotNone(bt_shareClose)
        if self.assertIsNotNone(bt_shareClose) == True:
            bt_shareClose.click()
            fd.write( "视频上传成功\n")
        else:
            fd.write( "视频上传失败\n")
        
    def test_03uploadVidoe(self):
        #导入视频并上传
        time.sleep(10)
        shoot_plus02 =self.driver.find_element_by_id("com.yixia.videoeditor:id/bottom_record")
        shoot_plus02.click()
        fd.write( "点击+按钮成功\n")
        time.sleep(5)
        bt_SCvideo = self.driver.find_element_by_id("com.yixia.videoeditor:id/upload_video_img")
        bt_SCvideo.click()
        time.sleep(5)
        fd.write( "点击上传视频按钮成功\n")
        time.sleep(5)
        bt_XCvideo=self.driver.find_element_by_class_name("android.widget.LinearLayout")
        bt_XCvideo.click()
        time.sleep(3)
        fd.write( "选择相册成功\n")
        bt_XCvideo02=self.driver.find_element_by_class_name("android.widget.ImageView")
        bt_XCvideo02.click()
        time.sleep(15)
        fd.write( "选择视频成功，进入节选视频界面\n")
        bt_know=self.driver.find_element_by_id("com.yixia.videoeditor:id/record_tip_ok")
        bt_know.click()
        time.sleep(5)
        fd.write( "点击知道了按钮成功\n")
        bt_title_RightNext = self.driver.find_element_by_id("com.yixia.videoeditor:id/titleRightTextView")
        bt_title_RightNext.click()
        time.sleep(10)
        fd.write( "进入预览界面\n")
        bt_title_Right02=self.driver.find_element_by_id("com.yixia.videoeditor:id/titleRight")
        bt_title_Right02.click()
        time.sleep(10)
        fd.write( "预览结束成功进入发布面板\n")
        bt_send = self.driver.find_element_by_id("com.yixia.videoeditor:id/share_video")
        bt_send.click()
        time.sleep(20)
        fd.write( "点击发布按钮成功\n")
        bt_shareClose02 = self.driver.find_element_by_id("com.yixia.videoeditor:id/upload_suc_dialog_close")
        self.assertIsNotNone(bt_shareClose02)
        if self.assertIsNotNone(bt_shareClose02) == True:
            bt_shareClose02.click()
            fd.write( "视频上传成功\n")
        else:
            fd.write( "视频上传失败\n")

    def tearDown(self):
        self.driver.quit()

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPTest('test_01login_phone'))
	suite.addTest(MPTest('test_02shoot'))
	suite.addTest(MPTest('test_03uploadVidoe'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)
