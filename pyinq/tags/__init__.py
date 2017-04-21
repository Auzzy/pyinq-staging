from pyinq.tags import _util
from pyinq.config import _DEFAULT_SUITE as DEFAULT_SUITE

__all__ = ["beforeSuite", "beforeModule", "beforeClass", "before", "after", "afterClass",
           "afterModule", "afterSuite", "test", "testClass", "skip", "skipIf", "skipUnless"]

def get_suite(suite=DEFAULT_SUITE):
	_util.build_suite(suite)
	return _util.get_suite(suite)

def finish_module(name):
	_util.finish_module(name)

##### FIXTURES #####

def beforeSuite(func=None, **kwargs):
	suite = kwargs["suite"] if "suite" in kwargs else None
	if func is None:
		return lambda func: _util.BeforeSuite_register(func,suite)
	else:
		return _util.BeforeSuite_register(func,suite)

def beforeModule(func):
	return _util.BeforeModule_register(func)

def beforeClass(func):
	return _util.BeforeClass_register(func)

def before(func):
	return _util.Before_register(func)

def after(func):
	return _util.After_register(func)

def afterClass(func):
	return _util.AfterClass_register(func)

def afterModule(func):
	return _util.AfterModule_register(func)

def afterSuite(func=None, **kwargs):
	suite = kwargs["suite"] if "suite" in kwargs else None
	if func is None:
		return lambda func: _util.AfterSuite_register(func,suite)
	else:
		return _util.AfterSuite_register(func,suite)

##### FIXTURE ALIASES #####
# These are deprecated, but will be maintained for now due to the initial
# release. They will be removed for version 1.0 at the latest.

BeforeSuite = beforeSuite
BeforeModule = beforeModule
BeforeClass = beforeClass
Before = before
After = after
AfterClass = afterClass
AfterModule = afterModule
AfterSuite = afterSuite

##### TESTS #####

def test(func=None, **kwargs):
	expected = kwargs["expect"] if "expect" in kwargs else None
	
	# DEPRECATED
	expected = kwargs["expected"] if not expected and "expected" in kwargs else expected
	
	suite = kwargs["suite"] if "suite" in kwargs else None

	if func is None:
		return lambda func: _util.Test_register(func,expected,suite)
	else:
		return _util.Test_register(func,expected,suite)


def testClass(cls=None, **kwargs):
	suite = kwargs["suite"] if "suite" in kwargs else None

	if cls is None:
		return lambda cls: _util.TestClass_register(cls,suite)
	else:
		return _util.TestClass_register(cls,suite)

##### TEST ALIASES #####
# These are deprecated, but will be maintained for now due to the initial
# release. They will be removed for version 1.0 at the latest.

Test = test
TestClass = testClass

##### SKIPS #####

def skip(func):
	return _util.Skip(func)

def skipIf(cond):
	return lambda func: _util.Skip(func,cond)

def skipUnless(cond):
	return lambda func: _util.Skip(func,not cond)

##### SKIP ALIASES #####
# These are deprecated, but will be maintained for now due to the initial
# release. They will be removed for version 1.0 at the latest.

Skip = skip
SkipIf = skipIf
SkipUnless = skipUnless

