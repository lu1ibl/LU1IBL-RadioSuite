"""
LU1IBL RadioSuite

Module Loader
"""

from __future__ import annotations

from radiosuite.modules.info import InfoModule


class ModuleLoader:
    """
    Descubre y carga los módulos disponibles.

    En RS-001 devuelve una lista fija.
    En RS-002 descubrirá automáticamente los módulos.
    """

    def load(self):

        return [
            InfoModule(),
        ]
