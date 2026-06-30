"""
LU1IBL RadioSuite

repeater.py

Modelo de datos de una repetidora.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Repeater:
    """Representa una repetidora de radio."""

    # Identificación
    call: str = ""
    owner: str = ""
    source: str = ""

    # Ubicación
    country: str = ""
    province: str = ""
    county: str = ""
    locality: str = ""

    # Frecuencias (MHz)
    output: float = 0.0
    input: float = 0.0
    offset: float = 0.0
    shift: str = ""

    # Operación
    tone: str = ""
    mode: str = ""
    digital_access: str = ""

    # Geografía
    latitude: float = 0.0
    longitude: float = 0.0
    locator: str = ""

    def has_coordinates(self) -> bool:
        """Indica si la repetidora tiene coordenadas válidas."""
        return self.latitude != 0.0 and self.longitude != 0.0

    def has_tone(self) -> bool:
        """Indica si tiene tono configurado."""
        return bool(self.tone.strip())

    def has_call(self) -> bool:
        """Indica si posee señal distintiva."""
        return bool(self.call.strip())

    def __str__(self) -> str:
        """Representación legible."""
        return (
            f"{self.call} "
            f"{self.output:.3f}/{self.input:.3f} MHz "
            f"{self.locality} ({self.country})"
        )
