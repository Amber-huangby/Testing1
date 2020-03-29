import pytest

@pytest.fixture(autouse=False)
def login():
    print('公用的登录')
    #yield
    print("yielddddddd之后的打印")
#
# @pytest.fixture()
def login2():
    print("login2222221")