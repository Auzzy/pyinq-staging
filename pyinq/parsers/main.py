from os.path import abspath,basename,dirname,isfile,join,splitext
from argparse import ArgumentParser,FileType

from pyinq import config
from pyinq.writers.html import HtmlReportWriter
from pyinq.writers.cli import CliReportWriter

NAME = "__main__"
_prog = None

def check_filepath(filepath):
	if not filepath:
		return None
	
	base_filename = basename(filepath)
	abs_dirname = dirname(abspath(filepath)) if base_filename else abspath(filepath)
	return join(abs_dirname, base_filename)

def check_isfile(filepath):
	return filepath if isfile(filepath) else None

def compose(parser=None, **kwargs):
	global _prog

	if not parser:
		parser = ArgumentParser(**kwargs)
	parser.add_argument("--config", type=check_isfile, default=None,
			help="Specify a PyInq config file.")
	parser.add_argument("--outfile", type=check_filepath, default=None,
			help="The destination for the output file. (default: ./<filename>_report)")
	parser.add_argument("--suite",default=config._DEFAULT_SUITE,
			help="The suite to run. If not provided, all tests are run.")
	
	writer_parser = parser.add_mutually_exclusive_group()
	writer_parser.add_argument("--html", action="store_true",
			help="Output the report using the built-in HTML Report Writer")
	writer_parser.add_argument("--cli", action="store_true",
			help="Output the report using the built-in CLI Report Writer")
	
	action_parser = parser.add_mutually_exclusive_group()
	action_parser.add_argument("--print", action="store_true", dest="print_",
			help="Write the report to the command line.")
	action_parser.add_argument("--write", action="store_true",
			help="Write the report to the file specified by outfile.")
	
	_prog = parser.prog
	
	return parser

def get_args(args):
	if args.config:
		execfile(args.config, dict())
	
	if args.suite is not None and args.suite != config._DEFAULT_SUITE:
		config.SUITE = args.suite
	
	if args.html:
		config.REPORT_WRITER = HtmlReportWriter
	elif args.cli:
		config.REPORT_WRITER = CliReportWriter
	if args.write:
		config.REPORT_ACTION = config.ActionEnum.WRITE
	elif args.print_:
		config.REPORT_ACTION = config.ActionEnum.PRINT
	
	if args.outfile:
		config.REPORT_OUTFILE = args.outfile
	elif config.REPORT_OUTFILE is None:
		test_filename = splitext(basename(_prog))[0] if _prog else "test"
		config.REPORT_OUTFILE = "{0}_report".format(test_filename)

	
	return {"outfile":config.REPORT_OUTFILE, "suite":config.SUITE}
