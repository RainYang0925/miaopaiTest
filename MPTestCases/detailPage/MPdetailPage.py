#coding:utf-8
'''
Created on 2016年10月12日
@author: wenjing
'''

import unittest
from appium import webdriver
from time import sleep
class MPdetailPage(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self, methodName)
        print '************************** MPdetailPage test **************************'

    def setUp(self):
        desired_caps={}
        desired_caps['device']='android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='4.4.2'
        desired_caps['deviceName']='69T7N15B26001273'

        #desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
        #被测试的App在电脑上的位置
        desired_caps['appPackage']='com.yixia.videoeditor'
        desired_caps['appActivity']='.ui.login.SplashActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def init_case(self):
        #处理开屏广告是否存在的情况
        try:
            sleep(1)
            el = self.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #获取开屏广告是否存在
            self.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #点击开屏广告上的'点击跳过'按钮
            sleep(2)
        except Exception,ex:
            pass

    def tearDown(self):
        self.driver.quit()
        print 'end ... '

    def test_check_like(self):
        print 'start test_check_like test ...  '
        self.init_case()
        sleep(5)
        #手机号登陆
        self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_record').click()
        sleep(5)
        try:
            self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click()
            sleep(5)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview').send_keys('13699193860')
            sleep(5)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview').send_keys('123456')
            sleep(5)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').is_enabled()
            self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()
            sleep(10)
        except:
            self.driver.keyevent('4')
            print'...........'
            sleep(10)
        


def suite(self):
    suite = unittest.TestSuite()  
    suite.addTest(MPdetailPage('test_check_like'))
    runner = unittest.TextTestRunner()  
    runner.run(suite)