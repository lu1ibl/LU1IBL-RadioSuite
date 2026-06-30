from radiosuite.version import VERSION


def test_version():
    assert VERSION.major == 0
    assert VERSION.minor == 1
    assert VERSION.patch == 0
    assert VERSION.short == "0.1.0"
