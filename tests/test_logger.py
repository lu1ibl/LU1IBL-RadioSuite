from pathlib import Path

from radiosuite.logger import create_logger


def test_logger():

    logger = create_logger(Path("logs"))

    logger.info("Logger funcionando")

    assert logger.name == "radiosuite"
