from pyinq import config
# from pyinq.writers.html import HtmlReportWriter

from report import CustomReportWriter

# config.REPORT_OUTFILE = "config_out.html"
# config.REPORT_ACTION = config.ActionEnum.WRITE
# config.REPORT_WRITER = HtmlReportWriter
config.REPORT_WRITER = CustomReportWriter
