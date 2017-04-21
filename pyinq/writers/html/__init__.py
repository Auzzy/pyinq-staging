import os.path

import markup

from pyinq.writers import ReportWriter

NBSP = "&nbsp;"
TAB = 4*NBSP
DEFAULT_CSSFILE = os.path.join(__path__[0], "default.css")

class HtmlReportWriter(ReportWriter):
	def __init__(self, title=None, options={}):
		super(HtmlReportWriter, self).__init__(title, options)
		self._read_options(options)

		self._page = markup.page()
		self._page.init(title=title)
		if self.style:
			self._page.style(self.style)
	
	def _read_options(self, options):
		if "style" in options:
			self.style = options["style"]
		else:
			cssfile = options["cssfile"] if "cssfile" in options and os.path.exists(options["cssfile"]) else None
			self.style = open(cssfile, 'r').read() if cssfile else None
		if not self.style:
			self.style = open(DEFAULT_CSSFILE, 'r').read() if os.path.exists(DEFAULT_CSSFILE) else None

	
	def start_suite(self, result, label=None):
		self._page.div(class_="suite")
		super(HtmlReportWriter, self).start_suite(result, label)
	
	def start_module(self, result, label=None):
		self._page.div(class_="module indent")
		super(HtmlReportWriter, self).start_module(result, label)
	
	def start_class(self, result, label=None):
		self._page.div(class_="class indent")
		super(HtmlReportWriter, self).start_class(result, label)
	
	def start_test(self, result, label=None):
		self._page.div(class_="test indent")
	
	def start_structure(self, result, label):
		if not result.is_default():
			text = "{label}: {name}".format(label=label.upper(), name=result.name)
			self._page.p(text, class_="section-header")
	
	def end_structure(self, result):
		self._page.div.close()


	def result_start(self, result, label):
		self._page.p(class_="result")
		text = "{label}: {name}".format(label=label.upper(), name=result.name)
		self._page.span(text, class_="result-header")
		self._newline()
	
	def result_asserts(self, result):
		self.result_status(result)
		super(HtmlReportWriter, self).result_asserts(result)
	
	def result_status(self, result):
		if result:
			status = result.get_status()
			if status is None:
				self._page.div("ERROR", class_="status error")
			elif status:
				self._page.div("PASSED", class_="status pass")
			else:
				self._page.div("FAILED", class_="status fail")
			self._newline()
	
	def result_end(self, result):
		self._page.p.close()

	def assert_result(self, result):
		result_html = self._assert_to_html(result)
		if result.result is None:
			self._page.div(str(result_html), class_="assert error")
		elif result.result:
			self._page.div(str(result_html), class_="assert pass")
		else:
			self._page.div(str(result_html), class_="assert fail")
	
	
	def _assert_to_html(self, result):
		assert_html = markup.page()
		result_str = str(result).replace(' ', NBSP).replace('\t', TAB)
		result_lines = result_str.splitlines()
		
		assert_html.add(result_lines[0])
		for line in result_lines[1:]:
			self.__newline(assert_html)
			assert_html.add(line)
		return assert_html

	def empty(self, result, label):
		fmt_str = "Default {label} empty" if result.is_default() else "{label} empty"
		self._page.span(fmt_str.format(label=label.capitalize()), class_="status warning")


	def _to_style(self, **kwargs):
		return '; '.join(["{0}:{1}".format(param.replace('_', '-'), kwargs[param]) for param in kwargs])
	

	def _newline(self):
		self.__newline(self._page)
	
	def __newline(self, page):
		page.br()
	
	def print_(self):
		print self._page
	
	def write(self, out):
		name,ext = os.path.splitext(out)
		if ext != "html":
			out = "{filename}.html".format(filename=name)

		print "Writing report to {0}".format(out)
		with open(out, 'w') as outfile:
			outfile.write(str(self))

	def __str__(self):
		return str(self._page)
