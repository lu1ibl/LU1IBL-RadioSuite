from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_csv_files_exist():

    csvs = sorted(DATA_DIR.glob("*.csv"))

    assert len(csvs) > 0, "No se encontraron archivos CSV."


def test_all_csv_can_be_opened():

    csvs = sorted(DATA_DIR.glob("*.csv"))

    for csv in csvs:

        df = pd.read_csv(csv)

        assert len(df) > 0, f"{csv.name} está vacío."

        assert len(df.columns) > 0, f"{csv.name} no tiene columnas."


def test_show_statistics():

    csvs = sorted(DATA_DIR.glob("*.csv"))

    total = 0

    print()

    print("=== RepeaterBook ===")

    for csv in csvs:

        df = pd.read_csv(csv)

        print(f"{csv.stem:15} {len(df):6} registros")

        total += len(df)

    print("-" * 30)

    print(f"TOTAL           {total:6}")
