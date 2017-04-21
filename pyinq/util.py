from traceback import extract_tb,format_list,format_exception_only
from os.path import relpath,split,splitext
from importlib import import_module
import os
import inspect

MODNAME = split(__file__)[0]

def create_tb_str(err_type, val, tb_list):
	header = "Traceback (most recent call last):\n"
	tb_str = "".join(format_list(tb_list))
	exc_str = "".join(format_exception_only(err_type,val)).strip()
	return header + tb_str + exc_str

### TODO: These two functions are only used by runner.
def _get_mod_name(path):
	rel_path = splitext(relpath(path,MODNAME))[0]
	rel_path = rel_path.replace(os.pardir,'.').replace(os.sep,'.')
	return '.' + rel_path

def get_trace_start(trace_obj):
	trace = extract_tb(trace_obj)
	for index,step in enumerate(trace):
		try:
			import_module(_get_mod_name(step[0]),"pyinq")
		except ValueError:
			return trace[index:]
	return []


### TODO: This function is only used by asserts._util.
def get_call_frame():
	for frame in inspect.stack():
		# The assert connecting pyinq to the test file will be outside pyinq.
		# Thus, if I try to import the test file relative to pyinq, it should
		# fail (with a ValueError). This gives me the proper frame.
		try:
			import_module(_get_mod_name(frame[1]),"pyinq")
		except ValueError:
			return frame
	return None

