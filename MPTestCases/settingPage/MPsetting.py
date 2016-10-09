#coding:utf-8
#Edit by liyuanhong 2016/4/12#
import unittest
from appium import webdriver
from time import sleep

class MPsetting(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print "************************** MPsetting test **************************"

	def init_case(self):
		#处理开屏广告是否存在的情况
		try:
			sleep(1)
			el = self.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #获取开屏广告是否存在
			self.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #点击开屏广告上的'点击跳过'按钮
			sleep(2)
		except Exception,ex:
			pass
		
	
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
		print 'end ... '

	#进入设置页面
	def test_into_setting_page(self):
		print 'start test_into_setting_page test ...  '
		'''按钮的点击测试
		1、分别对静音、wifi下自动播放、3G较底画质开关、静音进行了打开和关闭的点击测试
		'''
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
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
		
		'''新消息提醒
		1、分别对粉丝，评论，赞的push开关进行了打开和关闭
		'''
	def test_comment_etc(self):
		print 'start test_comment_etc test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_tips_text').click()  #点击新消息提醒
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_fans').click()  #打开新粉丝push
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_fans').click()  #关闭新粉丝push
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_comment').click()  #打开评论push
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_comment').click()  #关闭评论push
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_good').click()  #打开赞push
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/message_good').click()  #关闭赞push
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回按钮退出该页面
		sleep(1)

		'''语言设置
		1、主要测试了繁体中文，英文，简体中文之间的切换，以及判断语言是否改变
		'''
	def test_change_language(self):
		print 'start test_change_language test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_language_setting').click()  #点击语言设置
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_selectlanguage_traditional').click()  #点击繁体中文
		sleep(2)
		txt = self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').get_attribute("text")
		self.assertEqual(txt,u'我')
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_language_setting').click()  #点击语言设置
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_selectlanguage_english').click()  #点击Englist
		sleep(2)
		txt = self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').get_attribute("text")
		self.assertEqual(txt,'Me')
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_language_setting').click()  #点击语言设置
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_selectlanguage_simplified').click()  #点击简体中文
		sleep(2)
		txt = self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').get_attribute("text")
		self.assertEqual(txt,u'我')
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)

		'''手机绑定
		1、主要测试了进入手机号绑定和退出手机号绑定页面
		'''
	def test_bind_mobile(self):
		print 'start test_bind_mobile test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_bind').click()  #点击手机绑定
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #退出手机号绑定
		sleep(1)

		'''版本检测
		1、主要测试了版检测功能正常
		'''
	def test_version_check(self):
		print 'start test_version_check test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_name('版本检测').click()  #点击版本检测选项
		sleep(3)



		'''清空缓存
		1、主要检测点击情况缓存不清空
		2、点击清空缓存清空
		'''
	def test_clear_cache(self):
		print 'start test_clear_cache test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.find_element_by_name('清空缓存').click()  #点击清空缓存
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/dialog_left_buton').click()  #点击否取消清空缓存
		self.el = None
		try:
			self.el = self.driver.find_element_by_name('0')
		except Exception,ex:
			#print Exception,':',ex
			pass
		self.assertIsNone(self.el)  #通过缓存不为0来判断缓存没有清空
		sleep(2)
		self.driver.find_element_by_name('清空缓存').click()  #点击清空缓存
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/dialog_right_buton').click()  #点击是清空缓存
		sleep(1)
		self.el = None
		try:
			self.el = self.driver.find_element_by_name('0')
		except Exception,ex:
			#print Exception,':',ex
			pass
		self.assertIsNotNone(self.el)  #通过缓存为0来判断缓存已经被清空
		sleep(2)
		

	'''退出登陆
	1、点击退出登录
	'''
	def test_setting_page_all_button_click(self):
		print 'start test_setting_page_all_button_click test ...  '
		self.init_case()
		sleep(5)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
		sleep(2)
		self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
		sleep(1)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click() #我的页面点击设置
		sleep(2)
		self.driver.swipe(200,800,200,200,1000) #设置页面向上滑动
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/logout_button').click() #点击退出登录按钮
		sleep(2)

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPsetting('test_into_setting_page'))
	suite.addTest(MPsetting('test_comment_etc'))
	suite.addTest(MPsetting('test_change_language'))
	suite.addTest(MPsetting('test_bind_mobile'))
	suite.addTest(MPsetting('test_version_check'))
	suite.addTest(MPsetting('test_clear_cache'))
	suite.addTest(MPsetting('test_setting_page_all_button_click'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)

	