import os.path
import pkgutil
import imp

import tags

INIT = "__init__"
MAIN = "__main__"
SPECIAL = [INIT, MAIN]

def _load_tests(modules):
	for module in modules:
		execfile(module, dict())
		tags.finish_module(module)

def _find_and_add_module(modules, mod_name, pkg_path):
	try:
		mod_data = imp.find_module(mod_name, [pkg_path])
		modules.add(mod_data[1])
	except ImportError:
		pass

def _discover_modules(root, pattern):
	modules = set()
	for mod_info in pkgutil.iter_modules([root]):
		if mod_info[2]:
			submodules = _discover_modules(os.path.join(root, mod_info[1]), pattern)
			modules.update(submodules)
		elif mod_info[1] not in SPECIAL:
			_find_and_add_module(modules, mod_info[1], mod_info[0].path)
	return modules

def discover_tests(root=os.curdir, pattern=".*"):
	modules = _discover_modules(root, pattern)
	_load_tests(modules)


def get_suite(suite):
	return tags.get_suite(suite)
