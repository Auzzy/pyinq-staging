from pyinq.writers.cli import CliReportWriter

_DEFAULT_SUITE = None

class ActionEnum(object):
	PRINT = 1
	WRITE = 2


##### CONFIG VALUES #####
SUITE = _DEFAULT_SUITE

REPORT_TITLE = "Test Report"
REPORT_WRITER = CliReportWriter
REPORT_ACTION = ActionEnum.PRINT
REPORT_OUTFILE = "test_report"
REPORT_OPTIONS = {}

def build_writer():
	Writer = REPORT_WRITER
	return Writer(REPORT_TITLE, REPORT_OPTIONS)
