import random
import string

from model.project import Project


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.soap.get_projects_list("administrator", "root")
    project = Project(name=generate_random_string(15), description=generate_random_string(15))
    app.project.init_project(project)
    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)

