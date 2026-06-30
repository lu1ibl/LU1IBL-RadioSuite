"""
LU1IBL RadioSuite

logger.py

Sistema de logging centralizado.
"""

from __future__ import annotations

import logging
from pathlib import Path


def create_logger(log_dir: Path) -> logging.Logger:
    """
    Crea el logger principal de la aplicación.
    """

    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("radiosuite")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(
        log_dir / "builder.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger
