from seasons import getdate

def test_getdate():
    assert getdate("1970-01-01")==28504800
    assert getdate("2023-03-13")==527040
