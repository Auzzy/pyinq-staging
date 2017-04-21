from pyinq import discover_tests

suite = discover_tests('examples', suite="suite1")
if suite:
	report = suite()
	report.print_()
