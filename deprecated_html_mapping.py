from pyinq import discover_tests
from pyinq import printers
from pyinq.printers import html

suite = discover_tests('examples', suite="suite1", pattern="assert_tests")
if suite:
	report = suite()
	printers.print_report(report, html, html=open("deprecated_mapping.html", 'w'))
