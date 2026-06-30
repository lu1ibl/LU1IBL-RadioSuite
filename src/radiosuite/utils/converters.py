"""
Conversores seguros.
"""

from __future__ import annotations

import math


def to_float(value, default: float = 0.0) -> float:
    """
    Convierte cualquier valor a float.

    Si no puede, devuelve default.
    """

    if value is None:
        return default

    if isinstance(value, float):
        if math.isnan(value):
            return default
        return value

    text = str(value).strip()

    if text == "":
        return default

    try:
        return float(text)
    except ValueError:
        return default
