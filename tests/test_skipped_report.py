from pathlib import Path

from radiosuite.config import CONFIG
from radiosuite.modules.import_repeaterbook import ImportRepeaterBook
from radiosuite.project import Project

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_skipped_rows():

    project = Project(CONFIG)

    for csv in sorted(DATA_DIR.glob("*.csv")):

        ImportRepeaterBook(csv).run(project)

    print()

    print("Registros descartados:", len(project.skipped_rows))

    for row in project.skipped_rows:

        print(row)

    assert len(project.skipped_rows) == 1
