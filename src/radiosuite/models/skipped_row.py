"""
Registro descartado durante una importación.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SkippedRow:

    file: str
    row: int
    reason: str

    call: str = ""

    output: float = 0.0

    input: float = 0.0

    location: str = ""

    province: str = ""
