"""

Example tests for package two module two

"""


import sys
import datetime
import pytest


@pytest.mark.xdist_group(name="group1")
class TestsTwo:
    """

    All tests will run on the same worker if you pass '--dist loadgroup'

    """
    def test_two_example_1(self) -> None:
        """
        Example test 1
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        assert True

    def test_two_example_2(self) -> None:
        """
        Example test 2
        :return: None
        """
        print(datetime.datetime.now(), file=sys.stderr)
        assert True
