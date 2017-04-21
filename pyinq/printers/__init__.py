#############################
###   Deprecated in 0.3   ###
#############################
# This was the old print system. Although it worked, it was pretty terrible, so I've overhauled it. I recommend not using it for any new print modules, and converting any existing ones to the new system. See the PyInq docs for details on how.
# This print system will be removed for release 0.4.

import types

class AbstractPrinter(object):
	"""
	An abstract class for creating Printers, used to output the results
	of the executed tests.
	"""
	
	mess = "The \"{func}\" method is not implemented for the type {type}"

	def __init__(self, **kwargs):
		if type(self) is AbstractPrinter:
			raise TypeError("Can't instantiate the abstract base class AbstractPrinter")

	def title(self, name):
		"""Logs the report title."""
		name = self.__class__.__name__
		err = AbstractPrinter.mess.format(func="title",type=name)
		raise NotImplementedError(err)
	
	def section(self, label, name, nl=True):
		"""Logs a section header."""
		name = self.__class__.__name__
		err = AbstractPrinter.mess.format(func="section",type=name)
		raise NotImplementedError(err)

	def log_test(self, label, result):
		"""
		Logs the results of a single test (TestResult object),
		labeled with the provided label.
		"""
		name = self.__class__.__name__
		err = AbstractPrinter.mess.format(func="log_test",type=name)
		raise NotImplementedError(err)

	def log_fixture(self, label, result):
		"""
		Logs the results of a single test (TestResult object),
		labeled with the provided label.
		"""
		name = self.__class__.__name__
		err = AbstractPrinter.mess.format(func="log_fixture",type=name)
		raise NotImplementedError(err)

	def cleanup(self):
		"""Perform required cleanup operations, such as writing to a file."""

try:
	from pyinq.printers import cli
except:
	cli = None

try:
	from pyinq.printers import html
except:
	html = None

def get_default():
	return cli

def print_report(suite, printer_mod=None, **kwargs):
	def log_fixture(label, fixture):
		if fixture:
			printer.log_fixture(label,fixture)

	if type(printer_mod) is not types.ModuleType:
		print "Expected a module, but was given a {0}. Using the default printer as a result."
		printer_mod = get_default()
	
	try:
		printer = printer_mod.Printer(**kwargs)
	except:
		import sys
		print
		print "Could not create the \"Printer\" class: {0}".format(sys.exc_info()[1])
		print "Using the default printer."
		printer = get_default().Printer(**kwargs)

	try:
		printer.title("Test Report")

		log_fixture("Before Suite",suite.before)
		for module in suite:
			printer.section("Module",module.name,nl=False)
			log_fixture("Before Module",module.before)

			for cls in sorted(module, key=lambda cls: cls.name):
				printer.section("Class",cls.name)
				log_fixture("Before Class",cls.before)

				for test in sorted(cls, key=lambda test: test.name):
					before_label = "Before \"{0}\"".format(test.name)
					log_fixture(before_label,test.before)
					
					if not test.before or test.before[-1].result:
						printer.log_test("Test",test)
					
					after_label = "After \"{0}\"".format(test.name)
					log_fixture(after_label,test.after)

				log_fixture("After Class",cls.after)

			log_fixture("After Module",module.after)

		log_fixture("After Suite",suite.after)

	finally:
		printer.cleanup()
	
	print
	print "WARNING: This report was produced by the old printer system, which was deprecated in PyInq 0.3. It will be removed in PyInq 0.4. Please consider updating your code to the current system. This can be done by calling the \"print_()\" function on result object, which you passed in as the first argument to this function."
