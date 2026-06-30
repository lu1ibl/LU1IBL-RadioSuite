"""
LU1IBL RadioSuite

project.py

Objeto principal de la aplicación.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from logging import Logger
from typing import Any

from radiosuite.config import Config
from radiosuite.logger import create_logger
from radiosuite.models import Repeater, SkippedRow


@dataclass(slots=True)
class Project:
    """
    Contiene el estado global de la RadioSuite.
    """

    # Configuración global
    config: Config

    # Logger principal
    logger: Logger = field(init=False)

    # Base de datos de repetidoras
    repeaters: list[Repeater] = field(default_factory=list)

    # Base de datos de ciudades
    cities: list = field(default_factory=list)

    # Estadísticas de ejecución
    statistics: dict[str, Any] = field(default_factory=dict)

    # Caché
    cache: dict[str, Any] = field(default_factory=dict)

    # Módulos cargados
    modules: list = field(default_factory=list)

    # Filas descartadas durante la importación
    skipped_rows: list[SkippedRow] = field(default_factory=list)

    # Advertencias
    warnings: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Inicializa el proyecto."""

        self.logger = create_logger(self.config.logs_dir)
        self.logger.info("Proyecto inicializado.")

    @property
    def repeater_count(self) -> int:
        """Cantidad de repetidoras importadas."""
        return len(self.repeaters)

    @property
    def skipped_count(self) -> int:
        """Cantidad de registros descartados."""
        return len(self.skipped_rows)

    def add_warning(self, message: str) -> None:
        """Agrega una advertencia al proyecto."""

        self.warnings.append(message)
        self.logger.warning(message)
