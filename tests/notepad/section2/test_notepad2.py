import pytest

from src.base.testcase import BaseTest


class Test(BaseTest):
    test_details = pytest.mark.DETAILS(meta="Notepad Test experiment2",
                                       description="This test is just an experiment for Notepad",
                                       blocked_by="")

    @test_details
    def test_notepad2_1(self):
        assert 1 == 1
