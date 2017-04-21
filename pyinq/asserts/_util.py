from pyinq.results import TestResult
from pyinq.util import get_call_frame

results = None

def _assert_func(test, Result, Error):
	global results
	lineno,call = get_call()
	result = Result(lineno, call, test)
	if result.result:
		results.append(result)
	else:
		raise Error(lineno, call)

def _eval_func(test, Result):
	global results
	lineno,call = get_call()
	result = Result(lineno, call, test)
	results.append(result)

def clear_results():
	global results
	results = None

def init_results(test_name):
	global results
	results = TestResult(test_name)

def get_call():
	call_frame = get_call_frame()
	return call_frame[2],call_frame[4][0].strip()
