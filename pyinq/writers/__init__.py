from pyinq.writers.mixins import (DriverMixin, StartMixin, EndMixin, FixtureMixin,
				  FixtureResultMixin, TestResultMixin, EmptyMixin,
				  OutputMixin)

class ReportWriter(DriverMixin, StartMixin, EndMixin, FixtureMixin, FixtureResultMixin, TestResultMixin, EmptyMixin, OutputMixin):
	def __init__(self, title=None, options={}):
		super(ReportWriter, self).__init__()
		self.title = title if title else "Test Report"
		self.options = options
