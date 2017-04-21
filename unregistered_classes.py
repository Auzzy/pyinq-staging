from pyinq.tags import *

class Class1(object):
	@test
	def test1():
		print "Hello from Class1!"

class Class2(object):
	@test
	def test2():
		Class1.test1(Class1())

class Class3(object):
	@test
	def test3():
		print "test3 in class 3"

class Class4(object):
	@test
	def test3():
		print "test3 in class 4"
