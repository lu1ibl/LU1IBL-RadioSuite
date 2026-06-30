"""
LU1IBL RadioSuite

Generación del reporte de importación.
"""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from radiosuite.project import Project


class ImportReport:

    def generate(self, project: Project) -> Path:

        countries = Counter()
        modes = Counter()

        for repeater in project.repeaters:

            countries[repeater.country] += 1

            if repeater.mode:
                modes[repeater.mode] += 1

        report = {
            "generated_at": datetime.now().isoformat(),
            "repeaters": len(project.repeaters),
            "skipped": len(project.skipped_rows),
            "countries": dict(sorted(countries.items())),
            "modes": dict(modes.most_common()),
            "statistics": project.statistics,
        }

        filename = project.config.output_dir / "import_report.json"

        filename.parent.mkdir(parents=True, exist_ok=True)

        with filename.open("w", encoding="utf-8") as fp:
            json.dump(
                report,
                fp,
                indent=4,
                ensure_ascii=False,
            )

        project.logger.info("Reporte generado: %s", filename)

        return filename
