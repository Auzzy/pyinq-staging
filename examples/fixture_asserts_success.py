from pyinq.tags import *
from pyinq.asserts import *

@beforeClass
def setupClass():
	assert_true(True)

@before
def setup():
	assert_true(True)

@test
def test():
	print "TEST"
	assert_true(False)

@after
def teardown():
	assert_true("AFTER")

@afterClass
def teardownClass():
	assert_true(True)
