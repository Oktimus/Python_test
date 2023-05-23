[pytest]
markers =
    smoke: smoke tests
    sanity: sanity test
    str
    strtest

#Add the specified OPTS to the set of command line arguments as if they had been specified by the user.
addopts = --maxfail=5 -v

#collect tests from classes that end in Suite:
#python_classes = *Suite

#By default, files matching test_*.py and *_test.py will be considered test modules.
#python_files = example_*.py check_*.py test_*.py

#By default, pytest will consider any function prefixed with test as a test.
#Example of how to collect test functions and methods that end in _test:
#python_functions = *_test test* *_check

#files or test ids are given in the command line when executing pytest from the rootdir directory.
#testpaths = Pytest_topics\\py_fixtures

#List of fixtures that will be applied to all test functions;
#this is semantically the same to apply the @pytest.mark.usefixtures marker to all test functions.
#usefixtures =
#    setup_list