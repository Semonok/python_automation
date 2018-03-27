class SessionHelper:

    def __init__(self, application):
        self.application = application

    def login(self, username, password):
        wd = self.application.wd
        self.application.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form/input[3]").click()

    def logout(self):
        wd = self.application.wd
        wd.find_element_by_link_text("Logout").click()

