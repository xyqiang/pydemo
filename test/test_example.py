import pytest

class TestExample():
    def test_one(self):
        print("开始执行test_one方法")
        x = "this"
        pytest.assume("h" not in x)
        pytest.assume(1 == 2)
        pytest.assume("x" in "xxx")


    def test_two(self):
        print("开始执行test_two方法")
        x = "hello"
        assert "e" in x

    def test_three(self):
        print("开始执行test_three方法")
        a = "hello"
        b = "hello world"
        assert a not in b

class TestExample1():
    def test_a(self):
        print("开始执行test_a方法")
        x = "this"
        assert "h" in x

    def test_b(self):
        print("开始执行test_b方法")
        x = "hello"
        assert "e" in x

    def test_c(self):
        print("开始执行test_c方法")
        a = "hello"
        b = "hello world"
        assert a not in b

if __name__ == '__main__':
    pytest.main()
    pytest.main("-v -x TestExample")
    pytest.main(['-v','-x', 'TestExample'])