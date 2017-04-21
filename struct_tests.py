from pyinq.tags import *
from pyinq.asserts import *

@testClass
class Class1(object):
	@beforeClass
	def setupClass():
		print "setup Class1"
		assert_true(True)
	
	@before
	def setup():
		print "setup test in Class1"
		assert_true(True)
	
	@test
	def test1():
		print "test1 in Class1"
		assert_true(True)
	
	@test
	def test2():
		print "test2 in Class1"
		assert_true(True)

	@after
	def tearDown():
		print "tear down test in Class1"
		assert_true(True)
	
	@afterClass
	def tearDownClass():
		print "tear down Class1"
		assert_true(True)

@testClass
class Class2(object):
	@beforeClass
	def setupClass():
		print "setup Class2"
		assert_true(True)
	
	@before
	def setup():
		print "setup test in Class2"
		assert_true(True)
	
	@test
	def test1():
		print "test1 in Class2"
		assert_true(False)
	
	@after
	def tearDown():
		print "tear down test in Class2"
		assert_true(True)
	
	@afterClass
	def tearDownClass():
		print "tear down Class2"
		assert_true(True)
		Class2.raise_err()
	
	@staticmethod
	def raise_err():
		raise ValueError("ValueError")

@beforeModule
def setupModule():
	print "setup module"
	assert_true(True)

@afterModule
def tearDownModule():
	print "tear down module"
	assert_true(True)

@beforeClass
def setupMain():
	print "setup main"
	assert_true(True)
