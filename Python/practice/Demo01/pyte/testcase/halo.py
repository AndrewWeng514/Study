# @Date   : 2022/9/23 10:11
# @Author : Andrew
# @Name   : test_halo
import time

import pytest


class TestBaidu:
    @pytest.mark.login
    def testsearch(self):
        time.sleep(1)
        assert 1 == 2
