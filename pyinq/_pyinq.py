from pyinq import config,_discover,parsers
from pyinq.tests import run_tests
import pyinq._atexit as atexit

_discovery_enabled = True

def test_pyinq(**kwargs):
	atexit.unregister(_run_at_exit)
	run_tests()

def discover_tests_api(root, pattern=".*", suite=None):
	if _discovery_enabled:
		_discover_tests(root, pattern)
		return _discover.get_suite(suite)

def discover_tests_cmd(root, pattern=".*", **args):
	if _discovery_enabled:
		_discover_tests(root, pattern)
		run_all(args)

def _discover_tests(root, pattern):
	global _discovery_enabled
	atexit.unregister(_run_at_exit)
        _discovery_enabled = False
        _discover.discover_tests(root,pattern)
        _discovery_enabled = True

def _run_at_exit():
	args,name = parsers.get_args()
	if args:
		run_all(args)

def run_all(args):
	suite = _discover.get_suite(config.SUITE)
	
	report = suite()
	print
	
	if config.REPORT_ACTION == config.ActionEnum.PRINT:
		report.print_()
	else:
		report.write(config.REPORT_OUTFILE)
		
	
parsers.install_main_parser()
atexit.register(_run_at_exit)
