from __future__ import annotations

from typing import TYPE_CHECKING

from radiosuite.modules import BaseModule

if TYPE_CHECKING:
    from radiosuite.project import Project


class InfoModule(BaseModule):

    name = "Info"
    version = "0.1.0"
    description = "Información del sistema."

    def run(self, project: Project):

        project.logger.info("InfoModule ejecutado correctamente.")
