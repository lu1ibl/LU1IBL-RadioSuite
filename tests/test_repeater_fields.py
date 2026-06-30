from pathlib import Path

from radiosuite.config import CONFIG
from radiosuite.project import Project
from radiosuite.modules.import_repeaterbook import ImportRepeaterBook

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_repeater_fields():

    project = Project(CONFIG)

    csv = sorted(DATA_DIR.glob("*.csv"))[0]

    ImportRepeaterBook(csv).run(project)

    r = project.repeaters[0]

    assert r.call != ""
    assert r.output > 0
    assert r.input > 0
    assert r.country != ""
    assert r.source == "RepeaterBook"
