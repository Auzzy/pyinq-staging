from pyinq.tags import *

@testClass
class Class1(object):
	@beforeClass
	def setupClass():
		print "setup Class1"
	
	@before
	def setup():
		print "setup test in Class1"
	
	@test
	def test1():
		print "test1 in Class1"
	
	@test
	def test2():
		print "test2 in Class1"

	@after
	def tearDown():
		print "tear down test in Class1"
	
	@afterClass
	def tearDownClass():
		print "tear down Class1"

@testClass
class Class2(object):
	@beforeClass
	def setupClass():
		print "setup Class2"
	
	@before
	def setup():
		print "setup test in Class2"
	
	@test
	def test1():
		print "test1 in Class2"
	
	@after
	def tearDown():
		print "tear down test in Class2"
	
	@afterClass
	def tearDownClass():
		print "tear down Class2"

@beforeModule
def setupModule():
	print "setup module"

@afterModule
def tearDownModule():
	print "tear down module"

@beforeClass
def setupMain():
	print "setup main"
