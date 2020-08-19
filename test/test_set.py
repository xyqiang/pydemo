import pytest

@pytest.mark.search
def test_search1():
    print("test_search1")

@pytest.mark.search
def test_search2():
    print("test_search2")

@pytest.mark.search
def test_search3():
    print("test_search3")

@pytest.mark.login
def test_login1():
    print("test_login1")

@pytest.mark.login
def test_login2():
    print("test_login2")

if __name__ == '__main__':
    pytest.main()