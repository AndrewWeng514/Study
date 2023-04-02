# @Date   : 2022/9/23 15:58
# @Author : Andrew
# @Name   : main
import os

import pytest

pytest.main()

os.system("allure generate ./temp -o ./repot --clean")
