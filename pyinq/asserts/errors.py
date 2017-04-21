from pyinq.asserts.results import (AssertResult, AssertTruthResult,
		AssertEqualsResult, AssertInResult, AssertInstanceResult,
		AssertAttribResult, AssertRaisesResult, FailResult,
		ExpectedErrorResult, UnexpectedError)

##### ERRORS #####

class PyInqError(Exception):
	pass

class PyInqAssertError(PyInqError):
	def __init__(self, lineno, call):
		super(PyInqAssertError,self).__init__()
		self.lineno = lineno
		self.call = call
	
	def result(self):
		return AssertResult(self.lineno,self.call,False)

class PyInqAssertTruthError(PyInqAssertError):
	def __init__(self, lineno, call, value):
		super(PyInqAssertTruthError, self).__init__(lineno, call)
		self.value = value
	
	def result(self):
		return AssertTruthResult(self.lineno, self.call, False, self.value)

class PyInqAssertEqualsError(PyInqAssertError):
	def __init__(self, lineno, call, actual, expected):
		super(PyInqAssertEqualsError,self).__init__(lineno,call)
		self.actual = actual
		self.expected = expected
	
	def result(self):
		return AssertEqualsResult(self.lineno,self.call,False,self.actual,self.expected)

class PyInqAssertInError(PyInqAssertError):
	def __init__(self, lineno, call, item, collection):
		super(PyInqAssertInError,self).__init__(lineno,call)
		self.item = item
		self.collection = collection

	def result(self):
		return AssertInResult(self.lineno,self.call,False,self.item,self.collection)

class PyInqAssertInstanceError(PyInqAssertError):
	def __init__(self, lineno, call, obj, cls):
		super(PyInqAssertInstanceError,self).__init__(lineno,call)
		self.obj = obj
		self.cls = cls

	def result(self):
		return AssertInstanceResult(self.lineno,self.call,False,self.obj,self.cls)

class PyInqAssertAttribError(PyInqAssertError):
	def __init__(self, lineno, call, obj, attrib_name):
		super(PyInqAssertAttribError, self).__init__(lineno, call)
		self.obj = obj
		self.attrib_name = attrib_name

	def result(self):
		return AssertAttribResult(self.lineno, self.call, False, self.obj, self.attrib_name)

class PyInqAssertRaisesError(PyInqAssertError):
	def __init__(self, lineno, call, expected, func, args, kwargs):
		super(PyInqAssertRaisesError,self).__init__(lineno, call)
		self.expected = expected
		self.func = func
		self.args = args
		self.kwargs = kwargs

	def result(self):
		return AssertRaisesResult(self.lineno, self.call, "", self.expected, self.func, self.args, self.kwargs)

class PyInqFailError(PyInqError):
	def __init__(self, lineno, mess):
		super(PyInqFailError,self).__init__()
		self.lineno = lineno
		self.mess = mess

	def result(self):
		return FailResult(self.lineno,self.mess)
