#coding:utf-8
import unittest
import Params
from appium import webdriver
from time import sleep

class MPsetting(unittest.TestCase):
	def setUp(self):
		desired_caps={}
		desired_caps['device']='android'
		desired_caps['platformName']='Android'
		desired_caps['browserName']=''
		desired_caps['version']='4.4.2'
		desired_caps['deviceName']='HUAWEI H60-L01'

		#desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
		#被测试的App在电脑上的位置
		desired_caps['appPackage']='com.yixia.videoeditor'
		desired_caps['appActivity']='.ui.login.SplashActivity'
		self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

	def tearDown(self):
		self.driver.quit();

	def test_all_button_click(self):
		print 'test_all_button_click'
		sleep(10)

	def test_all_button_click1(self):
		print 'test_all_button_click1'

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPsetting('test_all_button_click'))
	suite.addTest(MPsetting('test_all_button_click1'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)

	