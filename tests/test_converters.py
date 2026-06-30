from radiosuite.utils.converters import to_float


def test_to_float():

    assert to_float("146.610") == 146.610

    assert to_float("0") == 0.0

    assert to_float("") == 0.0

    assert to_float(None) == 0.0

    assert to_float("x") == 0.0

    assert to_float("N/A") == 0.0
