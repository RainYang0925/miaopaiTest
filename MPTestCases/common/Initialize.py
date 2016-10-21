#coding:utf-8
#Edit by liyuanhong 2016/10/18#


#测试用例的初始化操作
def init_case(opt):
	#处理开屏广告是否存在的情况
	print "Initialize"
	try:
		sleep(1)
		el = opt.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #获取开屏广告是否存在
		opt.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #点击开屏广告上的'点击跳过'按钮
		sleep(2)
	except Exception,ex:
		pass