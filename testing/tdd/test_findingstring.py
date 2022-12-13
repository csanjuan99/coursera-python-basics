import findingstring, pytest


def test_ispresent():
    assert findingstring.ispresent("Al")

def test_nodigint():
    assert findingstring.nodigit("N7")