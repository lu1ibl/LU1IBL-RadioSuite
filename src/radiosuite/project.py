"""
LU1IBL RadioSuite

project.py

Objeto principal de la aplicación.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from logging import Logger

from radiosuite.config import Config
from radiosuite.logger import create_logger


@dataclass(slots=True)
class Project:
    """
    Contiene el estado global del proyecto.
    """

    config: Config

    logger: Logger = field(init=False)

    repeaters: list = field(default_factory=list)

    cities: list = field(default_factory=list)

    statistics: dict = field(default_factory=dict)

    cache: dict = field(default_factory=dict)

    modules: list = field(default_factory=list)

    def __post_init__(self) -> None:

        self.logger = create_logger(
            self.config.logs_dir
        )

        self.logger.info("Proyecto inicializado.")
