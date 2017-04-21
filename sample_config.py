from pyinq import config
from pyinq.printers.html import HtmlReportWriter

config.SUITE = "suite1"

config.REPORT_TITLE = "Config Report Writer"
config.REPORT_WRITER = HtmlReportWriter
config.REPORT_ACTION = config.ActionEnum.WRITE
config.REPORT_OUTFILE = "config_report.html"
config.REPORT_OPTIONS = {}
