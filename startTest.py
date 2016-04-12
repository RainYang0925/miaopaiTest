import unittest
import sys
import os

curDir = sys.path[0]

sys.path.append(curDir + '\\MPTestCases\\login')
sys.path.append(curDir + '\\MPTestCases\\shoot')
sys.path.append(curDir + '\\MPTestCases\\settingPage')
sys.path.append(curDir + '\\MPTestCases\\test')


import MPlogin
import MPshoot
import MPsetting
import MPTest


MPlogin.suite("0")
MPshoot.suite("0")
#MPTest.suite("0")
MPsetting.suite("0")
