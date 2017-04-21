from pyinq.config import build_writer,_DEFAULT_SUITE as DEFAULT_SUITE

class TestResultBase(list):
	def __init__(self, name):
		super(TestResultBase, self).__init__()
		self.name = name
		self.before = None
		self.after = None
	
	def __call__(self, writer=None):
		raise NotImplementedError("__call__() not overridden for type {0}. Should serve as the entry point into the writer framework.".format(type(self)))
	
	def is_default(self):
		return self.name == DEFAULT_SUITE
	
	def get_status(self):
		passing = True
		for result in self:
			status = self._result_status(result)
			if status is None:
				return None
			elif passing and not status:
				passing = False
		return passing

	def _result_status(self, result):
		raise NotImplementedError("All children of TestResultBase must implement _result_status")

	def print_(self, writer=None):
		writer = writer or build_writer()
		self(writer)
		writer.print_()
	
	def write(self, outfile, writer=None):
		writer = writer or build_writer()
		self(writer)
		writer.write(outfile)
	
class TestResultContainer(TestResultBase):
	def __init__(self, name, element_type):
		super(TestResultContainer, self).__init__(name)
		self.element_type = element_type

	def append(self, value):
		if not isinstance(value, self.element_type):
			element_type_name = self.element_type.__class__.__name__
			raise ValueError("Expected the value to be a {0} object. Type: {1}".format(element_type_name, type(value)))
		super(TestResultContainer, self).append(value)

	def _result_status(self, result):
		return result.get_status()
	
class TestResult(TestResultBase):
	def append(self, value):
		if isinstance(value, TestResultBase):
			raise ValueError("Cannot append another test result object. TestResult may only contain assert result objects.")
		super(TestResult, self).append(value)
	
	def _result_status(self, test):
		return test.result

	def __call__(self, writer=None):
		writer = writer or build_writer()
		return str(writer.test(self))

class TestClassResult(TestResultContainer):
	def __init__(self, name):
		super(TestClassResult, self).__init__(name, TestResult)
	
	def __call__(self, writer=None):
		writer = writer or build_writer()
		return str(writer.class_(self))

class TestModuleResult(TestResultContainer):
	def __init__(self, name):
		super(TestModuleResult, self).__init__(name, TestClassResult)

	def __call__(self, writer=None):
		writer = writer or build_writer()
		return str(writer.module(self))

class TestSuiteResult(TestResultContainer):
	def __init__(self, name):
		super(TestSuiteResult, self).__init__(name, TestModuleResult)

	def __call__(self, writer=None):
		writer = writer or build_writer()
		return str(writer.suite(self))
