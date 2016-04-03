import unittest
import sys
import os

curDir = sys.path[0]

sys.path.append(curDir + '\\MPTestCases\\login')
sys.path.append(curDir + '\\MPTestCases\\shoot')
sys.path.append(curDir + '\\MPTestCases\\settingPage')


import MPlogin
import MPshoot
import MPsetting


MPlogin.suite("0")
MPshoot.suite("0")
MPsetting.suite("0")
