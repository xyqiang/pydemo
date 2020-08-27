import pytest,yaml

@pytest.mark.parametrize(["a","b"], yaml.safe_load(open("datas/data.yaml")))
def test_data(a,b):
    print(a+b)