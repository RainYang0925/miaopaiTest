#coding:utf-8
#Edit by liyuanhong 2016/10/20#

from time import sleep

def init_login(self):
	#处理未登陆的情况
	sleep(5)
	self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my_lay').click() #点击底导上的我
	sleep(2)
	try:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/no_login_views').click() #点击我的页面顶部的个人信息栏弹出登陆对话框
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click() #点击手机号登陆
		sleep(2)
		#5、输入手机号
		e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview')
		e3.click()  #点击手机号输入框弹出键盘
		sleep(0.5)
		e3.send_keys('13699193860')
		sleep(2)
		#5、输入密码
		e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview')
		e3.click()  #点击密码输入框弹出键盘
		sleep(0.5)
		e3.send_keys('123456')
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click() #点击登陆
		sleep(2)
		try:
			self.driver.find_element_by_id('com.yixia.videoeditor:id/skip').click() #手机号绑定页面点击跳过
			sleep(2)
		except:
			pass
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #点击首页回到首页
		sleep(2)
	except:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #登陆状态则回到热门页面
		sleep(2)
		
		
		
		
		