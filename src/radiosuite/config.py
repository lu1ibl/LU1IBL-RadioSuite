"""
LU1IBL RadioSuite

config.py

Configuración global del proyecto.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Config:
    """Configuración global."""

    app_name: str = "LU1IBL RadioSuite"
    app_module: str = "Repeater Database Builder"

    root: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2])

    @property
    def input_dir(self) -> Path:
        return self.root / "input"

    @property
    def output_dir(self) -> Path:
        return self.root / "output"

    @property
    def cache_dir(self) -> Path:
        return self.root / "cache"

    @property
    def logs_dir(self) -> Path:
        return self.root / "logs"

    @property
    def docs_dir(self) -> Path:
        return self.root / "docs"

    @property
    def tests_dir(self) -> Path:
        return self.root / "tests"

    @property
    def examples_dir(self) -> Path:
        return self.root / "examples"

    @property
    def scripts_dir(self) -> Path:
        return self.root / "scripts"

    user_agent: str = "LU1IBL-RadioSuite/0.1"
    timeout: int = 20


CONFIG = Config()
