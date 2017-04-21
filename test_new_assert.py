from pyinq.tags import test
from pyinq.asserts import *

@test(suite="truth")
def test_assert_true():
	assert_true(5)

@test(suite="truth")
def test_assert_false():
	assert_false(1)

@test(suite="truth")
def test_eval_truth():
	eval_true(0)
	eval_false(9)

@test(suite="equal")
def test_assert_equal():
	assert_equal(4,5)

@test(suite="equal")
def test_assert_not_equal():
	assert_not_equal(4,5)

@test(suite="equal")
def test_eval_equal():
	eval_equal(4,5)
	eval_not_equal(4,5)

@test(suite="is")
def test_assert_is():
	assert_is(ValueError, Exception)

@test(suite="is")
def test_assert_is_not():
	assert_is_not(ValueError, IOError)

@test(suite="is")
def test_eval_is():
	eval_is(ValueError, Exception)
	eval_is_not(ValueError, Exception)

@test(suite="in")
def test_assert_in():
	assert_in(4, [1, 1, 2, 3, 5, 8, 13, 21])

@test(suite="in")
def test_assert_in_not():
	assert_not_in(4, [1, 1, 2, 3, 5, 8, 13, 21])

@test(suite="in")
def test_eval_in():
	eval_in(4, [1, 1, 2, 3, 5, 8, 13, 21])
	eval_not_in(4, [1, 1, 2, 3, 5, 8, 13, 21])

@test(suite="instance")
def test_assert_instance():
	assert_is_instance(ValueError(""), Exception)

@test(suite="instance")
def test_assert_not_instance():
	assert_is_not_instance(ValueError(""), IOError)

@test(suite="instance")
def test_eval_instance():
	eval_is_instance(ValueError(""), Exception)
	eval_is_not_instance(ValueError(""), Exception)

@test(suite="attrib")
def test_assert_attrib():
	assert_attrib(str(""), "low")

@test(suite="attrib")
def test_assert_not_attrib():
	assert_not_attrib(str(""), "lower")

@test(suite="attrib")
def test_eval_attrib():
	eval_attrib(str(""), "lower")
	eval_not_attrib(str(""), "lower")

@test(suite="none")
def test_assert_none():
	assert_none([])

@test(suite="none")
def test_assert_not_none():
	assert_not_none([])

@test(suite="none")
def test_eval_none():
	eval_none([])
	eval_not_none([])


def raise_value_error(one, two, four):
	raise ValueError("")

@test(suite="raises")
def test_assert_raises():
	assert_raises(ValueError, raise_value_error, 1, 2, four=6)

@test(suite="raises")
def test_eval_raises():
	eval_raises(ValueError, raise_value_error, 1, 2, four=6)
