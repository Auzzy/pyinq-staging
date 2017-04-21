import operator

from pyinq.asserts.results import (AssertResult, AssertTruthResult, AssertEqualsResult,
			AssertInResult, AssertInstanceResult, AssertAttribResult,
			AssertRaisesResult)
from pyinq.asserts.errors import (PyInqAssertError, PyInqAssertTruthError,
			PyInqAssertEqualsError,PyInqAssertInError, PyInqAssertInstanceError,
			PyInqAssertAttribError, PyInqAssertRaisesError, PyInqFailError)
from pyinq.asserts._util import _assert_func as assert_func, _eval_func as eval_func
from pyinq.asserts import _ops as ops

class _AssertFactory(object):
	def __init__(self, compare_func, Result, Error, arg_count):
		self.compare_func = compare_func

		def factory(*args):
			def result(lineno, call, result):
				return Result(lineno, call, result, *args)
			def error(lineno, call):
				return Error(lineno, call, *args)
			if arg_count != len(args):
				raise TypeError("Function takes exactly {0} arguments ({1} given)".format(arg_count, len(args)))
			return result,error
		self.Factory = factory

	def assert_(self, *args):
		return assert_func(self.compare_func(*args), *self.Factory(*args))

	def assert_not(self, *args):
		return assert_func(not self.compare_func(*args), *self.Factory(*args))

	def eval(self, *args):
		return eval_func(self.compare_func(*args), self.Factory(*args)[0])

	def eval_not(self, *args):
		return eval_func(not self.compare_func(*args), self.Factory(*args)[0])

truth_factory = _AssertFactory(operator.truth, AssertTruthResult, PyInqAssertTruthError, 1)
equal_factory = _AssertFactory(operator.eq, AssertEqualsResult, PyInqAssertEqualsError, 2)
is_factory = _AssertFactory(operator.is_, AssertEqualsResult, PyInqAssertEqualsError, 2)
in_factory = _AssertFactory(ops.in_, AssertInResult, PyInqAssertInError, 2) # operator.contains reverses the arguments, so it's useless to me
instance_factory = _AssertFactory(isinstance, AssertInstanceResult, PyInqAssertInstanceError, 2)
attrib_factory = _AssertFactory(hasattr, AssertAttribResult, PyInqAssertAttribError, 2)
raises_factory = _AssertFactory(ops.test_raises, AssertRaisesResult, PyInqAssertRaisesError, 4)
