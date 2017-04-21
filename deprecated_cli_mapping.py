from pyinq import discover_tests
from pyinq import printers
from pyinq.printers import cli

suite = discover_tests('examples', suite="suite1", pattern="assert_tests")
if suite:
	report = suite()
	printers.print_report(report, cli)
