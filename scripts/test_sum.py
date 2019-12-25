import pytest
import yaml,os,sys
sys.path.append(os.getcwd())

from data.read_data import read_yaml_data


def read_data():
    return [tuple(o) for i in read_yaml_data("sun_data.yml").values() for o in i]



class TestSum:
    @pytest.mark.parametrize("a,b,c",read_data())
    def test_sum(self, a, b, c):
        print(f"{a}+{b}={c}")
        assert a + b == c
