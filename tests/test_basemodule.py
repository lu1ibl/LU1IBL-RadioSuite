from radiosuite.modules import BaseModule
from radiosuite.project import Project
from radiosuite.config import CONFIG


class DummyModule(BaseModule):

    name = "Dummy"

    def run(self, project: Project):

        project.statistics["dummy"] = True


def test_basemodule():

    project = Project(CONFIG)

    module = DummyModule()

    module.initialize(project)
    module.run(project)
    module.finish(project)

    assert project.statistics["dummy"] is True
