import pytest

# 参数
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+3",5),("1+1",2)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected

# 组合参数
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[3,4,5])
def test_xy(x,y):
    print(f"参数组合x:{x},y:{y}")

# 方法名做参数
test_user_data=['xyq','lqm']
@pytest.fixture(scope='module')
def login_r(request):
    user = request.param
    print(f"打开首页准备登陆，用户{user}")
    return user

# @pytest.mark.skip() #跳过
# @pytest.mark.skipif(1==1,reason="跳过") #一定条件下跳过
# @pytest.mark.xfail()
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例返回{a}")
    assert a != ""

if __name__ == '__main__':
    pytest.main()




