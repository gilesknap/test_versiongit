import unittest

from versiongit_test.main import main


# https://github.com/bdarnell/plop/blob/master/plop/test/collector_test.py
class ProfilerTest(unittest.TestCase):
    assert main() == 42
