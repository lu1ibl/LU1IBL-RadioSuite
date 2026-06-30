from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data" / "repeaterbook"


def test_skipped_rows():

    print()
    print("=" * 70)
    print("REGISTROS DESCARTADOS")
    print("=" * 70)

    skipped = 0

    for csv in sorted(DATA_DIR.glob("*.csv")):

        df = pd.read_csv(csv)

        print(f"\n{csv.stem.upper()}")

        found = False

        for idx, row in df.iterrows():

            call = str(row.get("Call", "")).strip()

            if not call:

                found = True
                skipped += 1

                print(f"Fila : {idx + 2}")
                print(f"Call : '{call}'")
                print(f"TX   : {row.get('Output Freq')}")
                print(f"RX   : {row.get('Input Freq')}")
                print(f"Loc  : {row.get('Location')}")
                print("-" * 40)

        if not found:
            print("Sin registros descartados.")

    print()
    print(f"TOTAL DESCARTADOS : {skipped}")

    assert skipped >= 0
