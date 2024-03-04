from fuel import gauge 
from fuel import convert
import pytest

def test_fuel():
    # gauge返回的不应该是print，而应该是值！
    assert gauge(convert('3/4')) == "75%"
    assert gauge(convert('1/4')) == "25%"
    assert gauge(convert('4/4')) == "F"
    assert gauge(convert('0/4')) == "E"
    with pytest.raises(ValueError):
        convert("x/y")

    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ValueError):
        convert("10/3")

    with pytest.raises(ValueError):
        convert("1.5/4")

    with pytest.raises(ValueError):
        convert("5-4")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(2) == "2%"
    assert gauge(40) == "40%"
    assert gauge(98) == "98%"