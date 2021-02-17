from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def init_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_form(project)
        import time; time.sleep(2)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.open_project_page()
        self.project_cache = None

    def fill_project_form(self, project):
        self.change_value("name", project.project_name)
        self.change_value("description", project.description)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for row in wd.find_elements_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
                project_name = row.find_element_by_css_selector("td:nth-child(1)").text
                not_list = row.find_element_by_css_selector('a[href ^= "manage_proj_edit_page.php?project_id="]').get_attribute("href")
                id = not_list.replace("http://localhost/mantisbt-2.24.4/manage_proj_edit_page.php?project_id=", "")
                description = row.find_element_by_css_selector("td:nth-child(5)").text
                self.project_cache.append(Project(project_name=project_name, description=description, id=id))
        return list(self.project_cache)

    def del_project(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'a[href ^= "manage_proj_edit_page.php?project_id={str(id)}"]').click()