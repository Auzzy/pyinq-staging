from pyinq.tags import *
from pyinq.asserts import *

@testClass
@skip
class Test1(object):
	@beforeClass
	def init():
		eval_true(False)

	@test
	def test1():
		assert False
	
@skip
@testClass
class Test2:
	@beforeClass
	def init():
		eval_true(False)
	
	@test(suite="suite1")
	def test2():
		assert False
