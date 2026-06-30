"""
LU1IBL RadioSuite

builder.py

Punto de entrada principal de la aplicación.
"""

from __future__ import annotations

from radiosuite.config import CONFIG
from radiosuite.project import Project
from radiosuite.version import VERSION
from radiosuite.core.module_loader import ModuleLoader


def banner() -> None:
    """Muestra el banner de la aplicación."""

    print()
    print("=" * 60)
    print(" LU1IBL RadioSuite")
    print(" Repeater Database Builder")
    print(f" Versión {VERSION.full}")
    print("=" * 60)
    print()


def main() -> int:
    """Punto de entrada principal."""

    banner()

    project = Project(CONFIG)

    project.logger.info("Configuración cargada.")
    project.logger.info("Proyecto creado.")

    loader = ModuleLoader()

    modules = loader.load()

    project.logger.info(f"Módulos encontrados: {len(modules)}")

    for module in modules:

        project.logger.info(f"Inicializando módulo: {module.name}")

        module.initialize(project)

        project.logger.info(f"Ejecutando módulo: {module.name}")

        module.run(project)

        project.logger.info(f"Finalizando módulo: {module.name}")

        module.finish(project)

    print()
    print("Estado")
    print("-" * 60)
    print(f"Aplicación : {project.config.app_name}")
    print(f"Módulo     : {project.config.app_module}")
    print(f"Versión    : {VERSION.short}")
    print(f"Repetidoras: {len(project.repeaters)}")
    print(f"Ciudades   : {len(project.cities)}")
    print(f"Módulos    : {len(modules)}")
    print()

    print("RadioSuite inicializada correctamente.")
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
