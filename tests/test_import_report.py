from pathlib import Path
import json

from radiosuite.config import CONFIG
from radiosuite.core.import_report import ImportReport
from radiosuite.modules.import_repeaterbook import ImportRepeaterBook
from radiosuite.project import Project

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_import_report():

    project = Project(CONFIG)

    for csv in sorted(DATA_DIR.glob("*.csv")):
        ImportRepeaterBook(csv).run(project)

    report = ImportReport().generate(project)

    assert report.exists()

    with report.open("r", encoding="utf-8") as fp:
        data = json.load(fp)

    assert data["repeaters"] == len(project.repeaters)
    assert data["skipped"] == len(project.skipped_rows)

    assert "countries" in data
    assert "modes" in data
    assert "statistics" in data
