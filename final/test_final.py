import unittest
from final import getdate, road_fares, PDF

def test_getdate():
    assert getdate("2022-01-01", "2022-01-10") == 9
    assert getdate("2022-01-01", "2022-01-01") == 0

def test_road_fares():
    assert road_fares("1 2 3") == 6
    assert road_fares("1") == 1

def test_cb():
    pdf = PDF()
    pdf.add_page()
    effective_page_width = pdf.w - 2*pdf.l_margin
    pdf.chapter_body(effective_page_width, "test")


if __name__ == '__main__':
    unittest.main()
