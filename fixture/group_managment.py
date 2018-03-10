class GroupHelper:

    def __init__(self, applicaton):
        self.application = applicaton

    def open_group(self):
        wd = self.application.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_group(self):
        wd = self.application.wd
        wd.find_element_by_link_text("group page").click()

    def Create_new_group(self, group):
        wd = self.application.wd
        # Init group creation
        self.open_group()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.application.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_group(self):
        wd = self.application.wd
        self.open_group()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_group()

    def select_first_group(self):
        wd = self.application.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, Group):
        wd = self.application.wd
        self.open_group()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("update").click()
