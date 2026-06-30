"""
LU1IBL RadioSuite

Importador de archivos CSV de RepeaterBook.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from radiosuite.models import Repeater, SkippedRow
from radiosuite.modules import BaseModule
from radiosuite.project import Project
from radiosuite.utils.converters import to_float


class ImportRepeaterBook(BaseModule):
    """Importador de archivos CSV de RepeaterBook."""

    name = "ImportRepeaterBook"
    version = "0.3.0"
    description = "Importador de archivos CSV de RepeaterBook."

    def __init__(self, filename: Path):

        self.filename = Path(filename)

    def run(self, project: Project) -> None:

        project.logger.info("Leyendo %s", self.filename.name)

        df = pd.read_csv(self.filename)

        importadas = 0
        descartadas = 0

        for index, row in df.iterrows():

            call = str(row.get("Call", "")).strip()

            # Registro inválido
            if not call:

                descartadas += 1

                skipped = SkippedRow(
                    file=self.filename.name,
                    row=index + 2,
                    reason="missing_callsign",
                    call="",
                    output=to_float(row.get("Output Freq")),
                    input=to_float(row.get("Input Freq")),
                    location=str(row.get("Location", "")).strip(),
                    province=str(row.get("State", "")).strip(),
                )

                project.skipped_rows.append(skipped)

                project.logger.warning(
                    "Descartado %s fila %d: sin indicativo.",
                    self.filename.name,
                    index + 2,
                )

                continue

            repeater = Repeater(
                # Identificación
                call=call,
                owner="",
                source="RepeaterBook",
                # Ubicación
                country=self.filename.stem.capitalize(),
                province=str(row.get("State", "")).strip(),
                county=str(row.get("County", "")).strip(),
                locality=str(row.get("Location", "")).strip(),
                # Frecuencias
                output=to_float(row.get("Output Freq")),
                input=to_float(row.get("Input Freq")),
                offset=to_float(row.get("Offset")),
                # Operación
                tone=str(row.get("Uplink Tone", "")).strip(),
                mode=str(row.get("Modes", "")).strip(),
                digital_access=str(row.get("Digital Access", "")).strip(),
            )

            project.repeaters.append(repeater)

            importadas += 1

        project.statistics[self.filename.name] = {
            "importadas": importadas,
            "descartadas": descartadas,
            "total": len(df),
        }

        project.logger.info(
            "%s -> %d importadas, %d descartadas.",
            self.filename.stem,
            importadas,
            descartadas,
        )
