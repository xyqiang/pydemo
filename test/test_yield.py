import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("关闭浏览器")

def test_search1(open):
    print("test_search1")

def test_search2(open):
    print("test_search2")

def test_search3(open):
    print("test_search3")

if __name__ == '__main__':
    pytest.main()