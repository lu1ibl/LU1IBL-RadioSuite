from collections import Counter
from pathlib import Path

from radiosuite.config import CONFIG
from radiosuite.modules.import_repeaterbook import ImportRepeaterBook
from radiosuite.project import Project

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_data_quality():

    project = Project(CONFIG)

    for csv in sorted(DATA_DIR.glob("*.csv")):
        ImportRepeaterBook(csv).run(project)

    total = len(project.repeaters)

    no_call = 0
    no_locality = 0
    no_province = 0
    no_output = 0
    no_input = 0
    no_coordinates = 0

    modes = Counter()
    countries = Counter()

    for r in project.repeaters:

        if not r.call:
            no_call += 1

        if not r.locality:
            no_locality += 1

        if not r.province:
            no_province += 1

        if r.output <= 0:
            no_output += 1

        if r.input <= 0:
            no_input += 1

        if not r.has_coordinates():
            no_coordinates += 1

        if r.mode:
            modes[r.mode] += 1
        else:
            modes["(vacío)"] += 1

        countries[r.country] += 1

    print()
    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)

    print(f"Total repetidoras : {total}")
    print(f"Sin indicativo    : {no_call}")
    print(f"Sin localidad     : {no_locality}")
    print(f"Sin provincia     : {no_province}")
    print(f"Sin salida TX     : {no_output}")
    print(f"Sin entrada RX    : {no_input}")
    print(f"Sin coordenadas   : {no_coordinates}")

    print()
    print("Repetidoras por país")
    print("-" * 60)

    for country, qty in sorted(countries.items()):
        print(f"{country:15} {qty:5}")

    print()
    print("Modos")
    print("-" * 60)

    for mode, qty in modes.most_common():
        print(f"{mode:20} {qty:5}")

    # Validaciones mínimas
    assert total > 0
    assert total == sum(countries.values())
