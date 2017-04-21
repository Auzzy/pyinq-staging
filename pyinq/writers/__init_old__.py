class ReportWriter(object):
	def __init__(self, title=None, options={}):
		self.title = title if title else "Test Report"
		self.options = options
	

	def suite(self, result):
		return self.struct(result, self.start_suite, self.before_suite, self.module, self.after_suite, self.end_suite, self.empty_suite)

	def module(self, result):
		return self.struct(result, self.start_module, self.before_module, self.class_, self.after_module, self.end_module, self.empty_module)

	def class_(self, result):
		return self.struct(result, self.start_class, self.before_class, self.test, self.after_class, self.end_class, self.empty_class)

	def test(self, result):
		return self.test_struct(result, self.start_test, self.before_test, self.test_func, self.after_test, self.end_test)
	
	def struct(self, result, start, before, handler, after, end, empty):
		start(result)
		
		before(result.before)
		if result:
			for struct in sorted(result, key=lambda struct: struct.name):
				handler(struct)
		else:
			empty(result)
		after(result.after)

		end(result)
		
		return str(self)
	
	def test_struct(self, result, start, before, handler, after, end):
		start(result)

		before(result.before)
		if not result.before or result.before.get_status():
			handler(result)
		after(result.after)
		
		end(result)
		
		return str(self)
	
	
	def start_suite(self, result, label=None):
		label = label if label else "Suite"
		self.start_section(result, label)
	
	def start_module(self, result, label=None):
		label = label if label else "Module"
		self.start_section(result, label)
	
	def start_class(self, result, label=None):
		label = label if label else "Class"
		self.start_section(result, label)
	
	def start_test(self, result, label=None):
		label = label if label else "Test"
		self.start_section(result, label)
	
	def start_section(self, result, label):
		pass

	
	def end_suite(self, result):
		self.end_section(result)
	
	def end_module(self, result):
		self.end_section(result)
	
	def end_class(self, result):
		self.end_section(result)
	
	def end_test(self, result):
		self.end_section(result)
	
	def end_section(self, result):
		pass


	def before_suite(self, result, label=None):
		label = label if label else "Before Suite"
		self.suite_fixture(result, label)

	def after_suite(self, result, label=None):
		label = label if label else "After Suite"
		self.suite_fixture(result, label)

	def suite_fixture(self, result, label):
		self.fixture(result, label)

	def before_module(self, result, label=None):
		label = label if label else "Before Module"
		self.module_fixture(result, label)

	def after_module(self, result, label=None):
		label = label if label else "After Module"
		self.module_fixture(result, label)

	def module_fixture(self, result, label):
		self.fixture(result, label)

	def before_class(self, result, label=None):
		label = label if label else "Before Class"
		self.class_fixture(result, label)

	def after_class(self, result, label=None):
		label = label if label else "After Class"
		self.class_fixture(result, label)
	
	def class_fixture(self, result, label):
		self.fixture(result, label)

	def before_test(self, result, label=None):
		label = label if label else "Before"
		self.test_fixture(result, label)

	def after_test(self, result, label=None):
		label = label if label else "After"
		self.test_fixture(result, label)

	def test_fixture(self, result, label):
		self.fixture(result, label)

	
	def fixture(self, result, label):
		self.result(result, label, self.fixture_result_start, self.fixture_result, self.fixture_result_end)
	
	def fixture_result_start(self, result, label):
		self.result_start(result, label)

	def fixture_result(self, result):
		self.result_base(result)
	
	def fixture_result_end(self, result):
		self.result_end(result)
	
	def test_func(self, result, label=None):
		label = label if label else "Test"
		self.result(result, label, self.test_result_start, self.test_result, self.test_result_end)

	def test_result_start(self, result, label=None):
		label = label if label else "Test"
		self.result_start(result, label)

	def test_result(self, result):
		self.result_base(result)
	
	def test_result_end(self, result):
		self.result_end(result)


	def result(self, result, label, start, result_func, end):
		if result is not None:
			start(result, label)
			result_func(result)
			end(result)
	
	def result_start(self, result):
		pass

	def result_base(self, result):
		if result:
			self.assert_result(result[0])
			for assert_result in result[1:]:
				self._newline()
				self.assert_result(assert_result)
		else:
			self.empty_test(result)
	
	def result_end(self, result):
		self._newline()
	
	def assert_result(self, result):
		raise NotImplementedError("assert_result() not implemented for type {0}".format(type(self)))
	

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


	def _newline(self):
		raise NotImplementedError("_newline() not implemented for type {0}".format(type(self)))

	def print_(self):
		raise NotImplementedError("print_() not implemented for type {0}".format(type(self)))

	def write(self, outfile):
		raise NotImplementedError("write() not implemented for type {0}".format(type(self)))
	
	def __str__(self):
		raise NotImplementedError("__str__() not implemented for type {0}".format(type(self)))
