class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login_name, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(login_name)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self, login_name, password):
        if self.is_logged_in():
            if self.is_logged_in_as(login_name):
                return
            else:
                self.logout()
        self.login(login_name, password)

    def logout(self):
        wd = self.app.wd
        try:
            wd.find_element_by_css_selector("li[class='grey']")
            wd.find_element_by_css_selector("span[class='user-info']").click()
        except:
            pass
        wd.find_element_by_xpath("//a[contains(@href, '/mantisbt-2.24.4/logout_page.php')]").click()
        wd.find_element_by_name("username")

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("(//a[contains(@href, '#')])[2]")) > 0

    def is_logged_in_as(self, login_name):
        return self.get_logged_user() == login_name

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text
