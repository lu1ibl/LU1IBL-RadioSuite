"""
LU1IBL RadioSuite

Clase base para todos los módulos.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from radiosuite.project import Project


class BaseModule(ABC):
    """Clase base para todos los módulos."""

    name = "BaseModule"
    version = "0.1.0"
    description = ""

    def initialize(self, project: Project) -> None:
        """Inicialización opcional."""
        pass

    @abstractmethod
    def run(self, project: Project) -> None:
        """Ejecuta el módulo."""

    def finish(self, project: Project) -> None:
        """Finalización opcional."""
        pass
