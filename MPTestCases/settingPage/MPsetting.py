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
		print 'start setting page test >>>>'

	def tearDown(self):
		self.driver.quit();
		print 'end setting page test <<<<'

	#进入设置页面
	def test_into_setting_page(self):
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,800,200,200,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/wifi_setting').click() #打开wifi自动播放
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/wifi_setting').click() #关闭wifi自动播放
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/upload_3g_setting').click() #打开3G拍摄
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/upload_3g_setting').click() #关闭3G拍摄
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/mute_setting').click() #打开静音
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/mute_setting').click() #关闭静音
		sleep(1)


	def test_setting_page_all_button_click(self):
		print "test_setting_page_all_button_click"

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPsetting('test_into_setting_page'))
	#suite.addTest(MPsetting('test_setting_page_all_button_click'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)

	