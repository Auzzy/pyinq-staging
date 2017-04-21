from pyinq.asserts import _util
from pyinq.asserts._factory import (truth_factory, equal_factory, is_factory,
				  in_factory, instance_factory, attrib_factory,
				  raises_factory)
from pyinq.asserts.errors import PyInqFailError

__all__ = ["assert_true", "assert_false", "assert_none", "assert_not_none", "assert_equal",
           "assert_not_equal", "assert_is", "assert_is_not", "assert_in", "assert_not_in",
	   "assert_is_instance", "assert_is_not_instance", "assert_attrib", "assert_not_attrib",
	   "assert_raises", "eval_true", "eval_false", "eval_none", "eval_not_none", "eval_equal",
	   "eval_not_equal", "eval_is", "eval_is_not", "eval_in", "eval_not_in", "eval_is_instance",
	   "eval_is_not_instance", "eval_attrib", "eval_not_attrib", "eval_raises", "fail"]

##### ASSERTS #####

def assert_true(expr):
	return truth_factory.assert_(expr)
def assert_false(expr):
	return truth_factory.assert_not(expr)
def assert_none(expr):
	return is_factory.assert_(expr, None)
def assert_not_none(expr):
	return is_factory.assert_not(expr, None)
def assert_equal(actual, expected):
	return equal_factory.assert_(actual, expected)
def assert_not_equal(actual, expected):
	return equal_factory.assert_not(actual, expected)
def assert_is(actual, expected):
	return is_factory.assert_(actual, expected)
def assert_is_not(actual, expected):
	return is_factory.assert_not(actual, expected)
def assert_in(item, container):
	return in_factory.assert_(item, container)
def assert_not_in(item, container):
	return in_factory.assert_not(item, container)
def assert_is_instance(obj, cls):
	return instance_factory.assert_(obj, cls)
def assert_is_not_instance(obj, cls):
	return instance_factory.assert_not(obj, cls)
def assert_attrib(obj, name):
	return attrib_factory.assert_(obj, name)
def assert_not_attrib(obj, name):
	return attrib_factory.assert_not(obj, name)
def assert_raises(exception, func, *args, **kwargs):
	return raises_factory.assert_(exception, func, args, kwargs)


##### EVALS #####

def eval_true(expr):
	return truth_factory.eval(expr)
def eval_false(expr):
	return truth_factory.eval_not(expr)
def eval_none(expr):
	return is_factory.eval(expr, None)
def eval_not_none(expr):
	return is_factory.eval_not(expr, None)
def eval_equal(actual, expected):
	return equal_factory.eval(actual, expected)
def eval_not_equal(actual, expected):
	return equal_factory.eval_not(actual, expected)
def eval_is(actual, expected):
	return is_factory.eval(actual, expected)
def eval_is_not(actual, expected):
	return is_factory.eval_not(actual, expected)
def eval_in(item, container):
	return in_factory.eval(item, container)
def eval_not_in(item, container):
	return in_factory.eval_not(item, container)
def eval_is_instance(obj, cls):
	return instance_factory.eval(obj, cls)
def eval_is_not_instance(obj, cls):
	return instance_factory.eval_not(obj, cls)
def eval_attrib(obj, name):
	return attrib_factory.eval(obj, name)
def eval_not_attrib(obj, name):
	return attrib_factory.eval_not(obj, name)
def eval_raises(exception, func, *args, **kwargs):
	return raises_factory.eval(exception, func, args, kwargs)


##### FAIL #####

def fail(mess=""):
	lineno,_ = _util.get_call()
	raise PyInqFailError(lineno,mess)


##### ACCESS ######

def init(test_name):
	_util.init_results(test_name)

def clear():
	_util.clear_results()

def get_results():
	return _util.results

