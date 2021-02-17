from sys import maxsize

class Project:
    def __init__(self, project_name=None, description=None, id=None):
        self.project_name = project_name
        self.description = description
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize