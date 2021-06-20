import pytest

from utils.parsing import parse_paragraph_sep


def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"


def test_parse_paragraph_sep():
    data = {"14": {
        "lines": [
            "ANAKIN smiles as he blasts a TRADE FEDERATION DROID DROP FIGHTER."]},
        "15": {
            "lines": [
                "ANAKIN: There isn't a droid made that can out fly you, Master, and ",
                "no other way to get to the Chancellor . . ."
            ]},
        "16": {
            "lines": [
                "OBI-WAN: Look out, four droids inbound . . ."
            ]}}

    res = parse_paragraph_sep(data)
    assert len(res.keys()) == 2
    assert res['15']['actor'] == 'ANAKIN'
    assert res['16']['actor'] == 'OBI-WAN'

