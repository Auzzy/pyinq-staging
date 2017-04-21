from pyinq.writers.mixins import ResultMixin
from pyinq.writers.cli import CliReportWriter

class CustomResultMixin(ResultMixin):
	def assert_result(self, *args, **kwargs):
		print "OVER"

class CustomReportWriter(CliReportWriter, CustomResultMixin):
	pass
