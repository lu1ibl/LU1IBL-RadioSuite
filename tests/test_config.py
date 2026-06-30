from radiosuite.config import CONFIG


def test_directories():

    assert CONFIG.input_dir.name == "input"
    assert CONFIG.output_dir.name == "output"
    assert CONFIG.cache_dir.name == "cache"
    assert CONFIG.logs_dir.name == "logs"
