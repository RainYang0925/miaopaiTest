import unittest
import Params

class MPlogin(unittest.TestCase):
	def setUp(self):
		pass;

	def tearDown(self):
		pass;
	
	def test_login1(self):
		print "test_login1"

	def test_login2(self):
		print "test_login2"

	def test_login3(self):
		print "test_login3"

	def test_login4(self):
		print Params.A_params
		print Params.I_params

	def test_mobilePhone_login(self):
		pass

	def test_weibo_login(self):
		pass

	def test_weixin_login(self):
		pass

	def test_qq_login(self):
		pass


def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPlogin('test_login1'))  
	suite.addTest(MPlogin('test_login2'))  
	suite.addTest(MPlogin('test_login3'))
	suite.addTest(MPlogin('test_login4'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)


