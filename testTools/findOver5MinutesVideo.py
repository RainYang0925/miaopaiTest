#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import urllib
import json
from time import sleep
import types
import time

#根据suid获取用户名
def getUserName(suid):
	userName = ""
	#params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':'Z1fV~4uV6WRqfs3xndogdA__','version': '6.6.0.1','per':20})
	params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':suid,'version': '6.6.0.1','per':20})
	dat = urllib.urlopen("http://api.miaopai.com/m/space_user_info.json?%s" % params)
	jdat = json.loads(dat.read())
	userName = jdat['result']['header']['nick']
	#print userName
	return userName

#将以毫秒为单位的时间戳转换为日期格式
def convertToDate(timestamp):
	#theTime = jdat['result'][i]['channel']['ext']['finishTime']
	theDate = str(timestamp)[:-3]
	timeArray = time.localtime(int(theDate))
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	return otherStyleTime


#找首页频道超过5分钟的视频*****************************************
def testFenlei():
	categorys = [124,128]
	theMax = 0
	thecount = 1
	for cat in categorys:
		for var in range(1,4):
			#首页各个频道
			params = urllib.urlencode({'cateid': cat, 'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
			dat = urllib.urlopen("http://api.miaopai.com/m/cate2_channel.json?%s" % params)
			jdat = json.loads(dat.read())
			it = jdat['per']
			for i in range(0,it):
				judge = jdat['result'][i].has_key('color')
				if judge:
					pass
				else:
					theTime = jdat['result'][i]['channel']['ext']['length']
					#print theTime
					if theTime > theMax:
						theMax = theTime
					if theTime >= 300:
						print "channel : " + jdat['name'] + "第 " + str(var) + "页"
						print "时长 : " + str(theTime) + " 秒"
						print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
						print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
						print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
						print "t : " + jdat['result'][i]['channel']['ext']['t']
						print "ft : " + jdat['result'][i]['channel']['ext']['ft']
						print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
						print "***********************************************"
						print ""
					else:
						print str(thecount) + "  --  this video is less than 300 seconds !"
					thecount = thecount + 1
			sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#找热门超过5分钟的视频****************************************
def testHot():
	theMax = 0
	thecount = 1
	for var in range(1,10):
		#首页热门
		params = urllib.urlencode({'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v6_hot_channel.json?%s" % params)
		jdat = json.loads(dat.read())
		it = jdat['per']
		for i in range(0,it):
			judge = jdat['result'][i].has_key('color')
			if judge:
				pass
			else:
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "channel : " + "热门" + "第 " + str(var) + "页"
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					print "t : " + jdat['result'][i]['channel']['ext']['t']
					print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#找个人主页超过5分钟的视频***************************************
def testMyPage(suid):
	theMax = 0
	timeflag = 0
	page = 1
	thecount = 1
	while(int(timeflag) != -1):
		#print timeflag
		#params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':'Z1fV~4uV6WRqfs3xndogdA__','version': '6.6.0.1','timeflag':timeflag,'per':20})
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':suid,'version': '6.6.0.1','timeflag':timeflag,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/channel_forward_reward.json?%s" % params)
		jdat = json.loads(dat.read())
		timeflagOld = timeflag
		timeflag = jdat['result']['timeflag']
		it = jdat['result']['stream']['cnt']

		it = int(jdat['result']['stream']['cnt'])
		for i in range(0,it):
			judge = jdat['result']['stream']['list'][i].has_key('channel')
			#print judge
			if not judge:
				pass
			else:
				theTime = jdat['result']['stream']['list'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print getUserName(suid) + "第 " + str(page) + "页"
					print 'timeFlag : ' + str(timeflagOld)
					#print 'timeFlag : ' + str(jdat['result']['timeflag'])
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result']['stream']['list'][i]['channel']['stream']['base'] + ".mp4"
					print "time : " + jdat['result']['stream']['list'][i]['channel']['ext']['finishTimeNice']
					print "t : " + jdat['result']['stream']['list'][i]['channel']['ext']['t']
					print "ft : " + jdat['result']['stream']['list'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result']['stream']['list'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax



#找悬赏列表超过5分钟的视频***************************************
def testRewordList():
	theMax = 0
	page = 1
	thecount = 1
	rewordId = 0









#testFenlei()   #频道分类测试
#testHot()       #首页热门

#suid = 'Z1fV~4uV6WRqfs3xndogdA__'   #凡益网趣的suid
#suid = 'SBr3gTpwGbI53Lhyuz4xCg__'   #yiixia24000v的suid
#suid = 'AkwnpO4BXM4~G5BN' #远洪88的suid
suid = 'akaD2btl9Mvyf0MS'
testMyPage(suid)


























########################################################################################################################################
#http://api.miaopai.com/m/v6_hot_channel.json?token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&refresh=3&version=6.6.0.1&page=2&per=20   #热门接口
#http://api.miaopai.com/m/cate2_channel.json?cateid=128&token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&version=6.6.0.1&page=1&per=20   #频道接口
#http://api.miaopai.com/m/channel_forward_reward.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&suid=Z1fV~4uV6WRqfs3xndogdA__&version=6.6.0.1&timeflag=1475982730748&per=20 #个人主页
#http://api.miaopai.com/m/space_user_info.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&suid=Z1fV~4uV6WRqfs3xndogdA__  #个人页面个人信息


#悬赏列表 ---- 可测试
#关注页面 ---- 可测试 ----  有方法
#同城页面 ---- 可测试
#话题页面 ---- 可测试 ----  有方法
#悬赏页面 ---- 可测试
#视频合集 ---- 可测试
#搜索页面 ---- 可测试 ----  有方法
#个人主页 ---- 可测试 ----  ok
#热榜页面 ---- 可测试 ----  ok（最后一个视频都不在8月1号之前）
#频道分类页面 
#发现页面 ---- 排除（只包含话题和合集）
#频道达人视频封面 ----  可测试 ----  有方法（后台配置一个大于5分钟的视频）



