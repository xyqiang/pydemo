import pytest,yaml

from pycode.calc import Calc


class TestCalc():
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("data1,data2,expect",yaml.safe_load(open("./datas/data.yaml")))
    def test_add(self,data1,data2,expect):
        result = self.calc.add(data1,data2)
        assert result == expect


    def test_addstep(self):
        steps = yaml.safe_load(open("./datas/step.yaml"))
        for step in steps:
            print(f"step--->{step}")
            if "add1" in step:
                result = self.calc.add1(-1,-2)
                assert result == -3
            elif "add2" in step:
                result = self.calc.add2(0.5,0.5)
                assert result == 1
