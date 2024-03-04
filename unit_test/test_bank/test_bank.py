from bank import value

def test_value():
    # 注意函数最好有返回值
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100
