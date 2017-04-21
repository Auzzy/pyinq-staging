from sys import exc_info

from pyinq.util import create_tb_str,get_trace_start
from pyinq.asserts.errors import PyInqAssertError, PyInqFailError
from pyinq.asserts.results import ExpectedErrorResult,UnexpectedError
from pyinq import asserts

def handle_error(expected):
	exc_type,exc_value,trace_obj = exc_info()[:3]
	trace = get_trace_start(trace_obj)
	if expected and isinstance(exc_value,expected):
		lineno = trace[0][1]
		result = ExpectedErrorResult(True,expected,lineno)
		halt = False
	else:
		tb_str = create_tb_str(exc_type,exc_value,trace)
		result = UnexpectedError(tb_str)
		halt = True
	return result,halt

def handle_assert(test):
	try:
		test()
	except AssertionError:
		trace = get_trace_start(exc_info()[2])[0]
		lineno = trace[1]
		call = trace[3]
		raise PyInqAssertError(lineno,call)

def _test_runner(test):
	if test:
		halt = False
		expected = hasattr(test,"expected") and test.expected
		assert_results = []
		asserts.init(test.name)
		
		try:
			handle_assert(test)
		except (PyInqAssertError, PyInqFailError) as mess:
			result = mess.result()
			assert_results.append(result)
			halt = True
		except Exception:
			result,halt = handle_error(expected)
			assert_results.append(result)
		else:
			if expected:
				result = ExpectedErrorResult(False,expected)
				assert_results.append(result)
				halt = True
		finally:
			assert_results[:0] = asserts.get_results()
			asserts.clear()
		
		return test.name,assert_results,halt
	else:
		return None,None,False

def run_fixture(test):
	return _test_runner(test)

def run_test(test):
	return _test_runner(test)[:-1]
