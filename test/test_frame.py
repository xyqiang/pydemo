import pytest

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_function():
    print("test_function")
    assert 1 == 1


class TestFrame():
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_frame(self):
        print("test_frame")
        assert 2== 2

if __name__ == '__main__':
    pytest.main("-v -s")
