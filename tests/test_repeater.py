from radiosuite.models import Repeater


def test_repeater():

    r = Repeater()

    r.call = "LU1IBL"

    r.country = "Argentina"

    r.output = 146.610

    assert r.call == "LU1IBL"

    assert r.output == 146.610
