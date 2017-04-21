from pyinq.asserts import assert_true
from pyinq.tags import *

@before
def setup():
	print "SETUP TEST2"

@testClass
class Class1(object):
	@before
	def setup():
		print "SETUP TEST1"

	@test(suite="suite1")
	def test1():
		assert_true(True)
	

@test(suite="suite1")
def test2():
	assert_true(True)
