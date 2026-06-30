from pathlib import Path

from radiosuite.config import CONFIG
from radiosuite.modules.import_repeaterbook import ImportRepeaterBook
from radiosuite.project import Project


def test_importer_creation():

    module = ImportRepeaterBook(Path("input/test.csv"))

    project = Project(CONFIG)

    assert module.name == "ImportRepeaterBook"

    assert project.repeaters == []
