"""
LU1IBL RadioSuite

version.py

Información de versión del proyecto.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    """Representa la versión de la aplicación."""

    major: int
    minor: int
    patch: int
    codename: str

    @property
    def short(self) -> str:
        """Versión corta."""
        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def full(self) -> str:
        """Versión completa."""
        return f"{self.short} ({self.codename})"


VERSION = Version(major=0, minor=1, patch=0, codename="RS-001 Foundation")
