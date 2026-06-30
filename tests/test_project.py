from radiosuite.config import CONFIG
from radiosuite.project import Project


def test_project():

    project = Project(CONFIG)

    assert project.config.app_name == "LU1IBL RadioSuite"

    assert isinstance(project.repeaters, list)

    assert isinstance(project.cities, list)

    assert isinstance(project.statistics, dict)
