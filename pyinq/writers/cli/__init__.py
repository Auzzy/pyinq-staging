from StringIO import StringIO

from pyinq.writers import ReportWriter
from pyinq.writers.cli.printer import print_,to_str,to_plaintext
from pyinq.writers.cli import colors

class CliReportWriter(ReportWriter):
	def __init__(self, title=None, options={}):
		super(CliReportWriter, self).__init__(title, options)
		self._output = ""
		self._append("REPORT: " + str(title))
		self._newline()
	
	def start_module(self, result, label=None):
		super(CliReportWriter, self).start_module(result)
		self._newline()

	def start_test(self, result, label=None):
		pass

	def start_structure(self, result, label):
		if not result.is_default():
			text = "{label}: {name}".format(label=label.upper(), name=result.name)
			self._append(text, fore=colors.BLACK, back=colors.WHITE, bright=False)
	
	def end_module(self, result):
		self.start_structure(result, "END")
		self._newline()


	def empty(self, result, label):
		fmt_str = "DEFAULT {label} EMPTY" if result.is_default() else "{label} EMPTY"
		self._append(fmt_str.format(label=label.upper()), fore=colors.BLACK, back=colors.WARNING, bright=False)

	
	def result_start(self, result, label):
		self._append("{label}: {name}".format(label=label, name=result.name))
	
	def result_asserts(self, result):
		self.result_status(result)
		super(CliReportWriter, self).result_asserts(result)
	
	def result_end(self, result):
		self._newline()
		self._newline()
	
	def result_status(self, result):
		if result:
			status = result.get_status()
			if status is None:
				self._append("ERROR", back=colors.ERROR)
			elif status:
				self._append("PASSED", back=colors.PASS)
			else:
				self._append("FAILED", back=colors.FAIL)

	def assert_result(self, assert_result):
		if assert_result.result is None:
			self._append(assert_result, fore=colors.ERROR, bright=True, nl=False)
		elif assert_result.result:
			self._append(assert_result, fore=colors.PASS, bright=True, nl=False)
		else:
			self._append(assert_result, fore=colors.FAIL, bright=True, nl=False)
	
	
	def _append(self, text, fore=None, back=None, bright=None, nl=True):
		kwargs = {}
		if fore is not None:
			kwargs["fore"] = fore
		if back is not None:
			kwargs["back"] = back
		if bright is not None:
			kwargs["bright"] = bright
		self._output += to_str(text, **kwargs)
		if nl:
			self._newline()
	
	def _newline(self):
		self._output += '\n'
	
	def print_(self):
		print str(self)
	
	def write(self, out):
		plaintext = to_plaintext(str(self))
		print "Writing report to {0}".format(out)
		with open(out, 'w') as outfile:
			outfile.write(plaintext)
	
	def __str__(self):
		return str(self._output)
