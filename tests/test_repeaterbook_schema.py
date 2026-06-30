from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_show_csv_schema():

    csvs = sorted(DATA_DIR.glob("*.csv"))

    print()

    print("=" * 70)

    print("ESQUEMA DE COLUMNAS")

    print("=" * 70)

    schemas = {}

    for csv in csvs:

        df = pd.read_csv(csv, nrows=1)

        cols = list(df.columns)

        schemas[csv.stem] = cols

        print(f"\n{csv.stem.upper()}")

        for c in cols:
            print(f"  - {c}")

    # Todas las columnas encontradas
    all_columns = sorted({col for cols in schemas.values() for col in cols})

    print("\n" + "=" * 70)
    print("COLUMNAS ÚNICAS")
    print("=" * 70)

    for c in all_columns:
        print(c)
