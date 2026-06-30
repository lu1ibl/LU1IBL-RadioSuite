"""
LU1IBL RadioSuite

builder.py

Punto de entrada principal de la aplicación.
"""

from __future__ import annotations

from radiosuite.config import CONFIG
from radiosuite.project import Project
from radiosuite.version import VERSION


def banner() -> None:
    print()
    print("=" * 60)
    print(" LU1IBL RadioSuite")
    print(" Repeater Database Builder")
    print(f" Versión {VERSION.full}")
    print("=" * 60)
    print()


def main() -> int:

    banner()

    project = Project(CONFIG)

    project.logger.info("Configuración cargada.")
    project.logger.info("Proyecto creado.")
    project.logger.info("Sin módulos cargados.")

    print()
    print("Estado")
    print("-" * 60)
    print(f"Aplicación : {project.config.app_name}")
    print(f"Módulo     : {project.config.app_module}")
    print(f"Versión    : {VERSION.short}")
    print(f"Repetidoras: {len(project.repeaters)}")
    print(f"Ciudades   : {len(project.cities)}")
    print()
    print("RadioSuite inicializada correctamente.")
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
