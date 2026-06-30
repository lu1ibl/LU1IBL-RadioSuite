from pathlib import Path

from radiosuite.config import CONFIG
from radiosuite.modules.import_repeaterbook import ImportRepeaterBook
from radiosuite.project import Project

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_statistics_match_repeaters():

    project = Project(CONFIG)

    total = 0

    for csv in sorted(DATA_DIR.glob("*.csv")):

        importer = ImportRepeaterBook(csv)
        importer.run(project)

        stats = project.statistics[csv.name]

        total += stats["importadas"]

        assert stats["importadas"] + stats["descartadas"] == stats["total"]

    assert total == len(project.repeaters)
