class StartMixin(object):
	def start_suite(self, result, label=None):
		label = label if label else "Suite"
		self.start_structure(result, label)
	
	def start_module(self, result, label=None):
		label = label if label else "Module"
		self.start_structure(result, label)
	
	def start_class(self, result, label=None):
		label = label if label else "Class"
		self.start_structure(result, label)
	
	def start_test(self, result, label=None):
		label = label if label else "Test"
		self.start_structure(result, label)
	
	def start_structure(self, result, label):
		pass

class EndMixin(object):
	def end_suite(self, result):
		self.end_structure(result)
	
	def end_module(self, result):
		self.end_structure(result)
	
	def end_class(self, result):
		self.end_structure(result)
	
	def end_test(self, result):
		self.end_structure(result)
	
	def end_structure(self, result):
		pass

class FixtureMixin(object):
	def before_suite(self, result, label=None):
		label = label if label else "Before Suite"
		self.suite_fixture(result, label)

	def after_suite(self, result, label=None):
		label = label if label else "After Suite"
		self.suite_fixture(result, label)

	def suite_fixture(self, result, label):
		self.base_fixture(result, label)

	def before_module(self, result, label=None):
		label = label if label else "Before Module"
		self.module_fixture(result, label)

	def after_module(self, result, label=None):
		label = label if label else "After Module"
		self.module_fixture(result, label)

	def module_fixture(self, result, label):
		self.base_fixture(result, label)

	def before_class(self, result, label=None):
		label = label if label else "Before Class"
		self.class_fixture(result, label)

	def after_class(self, result, label=None):
		label = label if label else "After Class"
		self.class_fixture(result, label)
	
	def class_fixture(self, result, label):
		self.base_fixture(result, label)

	def before_test(self, result, label=None):
		label = label if label else "Before"
		self.test_fixture(result, label)

	def after_test(self, result, label=None):
		label = label if label else "After"
		self.test_fixture(result, label)

	def test_fixture(self, result, label):
		self.base_fixture(result, label)
	
	def base_fixture(self, result, label):
		self.fixture_result(result, label)

class ResultMixin(object):
	def result(self, result, label, start, asserts, end):
		if result is not None:
			start(result, label)
			asserts(result)
			end(result)
	
	def result_start(self, result, label):
		pass

	def result_asserts(self, result):
		if result:
			self.assert_result(result[0])
			for assert_result in result[1:]:
				self._newline()
				self.assert_result(assert_result)
		else:
			self.empty_test(result)
	
	def result_end(self, result):
		pass
	
	def assert_result(self, assert_result):
		raise NotImplementedError("assert_result() not implemented")

class FixtureResultMixin(ResultMixin):
	def fixture_result(self, result, label):
		self.result(result, label, self.fixture_result_start, self.fixture_result_asserts, self.fixture_result_end)
	
	def fixture_result_start(self, result, label):
		self.result_start(result, label)

	def fixture_result_asserts(self, result):
		self.result_asserts(result)
	
	def fixture_result_end(self, result):
		self.result_end(result)

class TestResultMixin(ResultMixin):
	def test_result(self, result, label=None):
		label = label if label else "Test"
		self.result(result, label, self.test_result_start, self.test_result_asserts, self.test_result_end)

	def test_result_start(self, result, label=None):
		label = label if label else "Test"
		self.result_start(result, label)

	def test_result_asserts(self, result):
		self.result_asserts(result)
	
	def test_result_end(self, result):
		self.result_end(result)

class EmptyMixin(object):
	def empty_suite(self, result, label=None):
		label = label if label else "Suite"
		self.empty(result, label)

	def empty_module(self, result, label=None):
		label = label if label else "Module"
		self.empty(result, label)

	def empty_class(self, result, label=None):
		label = label if label else "Class"
		self.empty(result, label)
	
	def empty_test(self, result, label=None):
		label = label if label else "Test"
		self.empty(result, label)
	
	def empty_fixture(self, result, label=None):
		label = label if label else "Fixture"
		self.empty(result, label)

	def empty(self, result, label):
		pass

class DriverMixin(object):
	def suite(self, result):
		handler = lambda result: self._struct_handler(result, self.module, self.empty_suite)
		return self.struct(result, self.start_suite, self.before_suite, handler, self.after_suite, self.end_suite)

	def module(self, result):
		handler = lambda result: self._struct_handler(result, self.class_, self.empty_module)
		return self.struct(result, self.start_module, self.before_module, handler, self.after_module, self.end_module)

	def class_(self, result):
		handler = lambda result: self._struct_handler(result, self.test, self.empty_class)
		return self.struct(result, self.start_class, self.before_class, handler, self.after_class, self.end_class)

	def test(self, result):
		handler = lambda result: self._test_handler(result, self.test_result)
		return self.struct(result, self.start_test, self.before_test, handler, self.after_test, self.end_test)
	
	def struct(self, result, start, before, handler, after, end):
		start(result)
		before(result.before)
		handler(result)
		after(result.after)
		end(result)
		
		return str(self)
	
	def _struct_handler(self, result, handler, empty):
		if result:
			for struct in sorted(result, key=lambda struct: struct.name):
				handler(struct)
		else:
			empty(result)

	def _test_handler(self, result, handler):
		if not result.before or result.before.get_status():
			handler(result)
	
class OutputMixin(object):
	def _newline(self):
		raise NotImplementedError("_newline() not implemented")

	def print_(self):
		raise NotImplementedError("print_() not implemented")

	def write(self, outfile):
		raise NotImplementedError("write() not implemented")
