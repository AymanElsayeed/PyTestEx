"""

Example tests for package one module one

"""

import sys
import datetime
import pytest


@pytest.mark.xdist_group(name="group1")
class TestsOne:
    """
    All tests will run on the same worker if you pass '--dist loadgroup'
    """
    def test_one_example_1(self):
        print(datetime.datetime.now(), file=sys.stderr)
        assert True

    def test_one_example_2(self):
        print(datetime.datetime.now(), file=sys.stderr)
        assert True