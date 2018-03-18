from model.group import Group
from selenium.common.exceptions import NoSuchElementException


class GroupHelper:

    def __init__(self, applic):
        self.application = applic

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
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text_name):
        wd = self.application.wd
        if text_name is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text_name)

    def delete_group(self, index):
        wd = self.application.wd
        self.select_group(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group()
        self.group_cache = None

    def select_group(self, index):
        wd = self.application.wd
        self.open_group()
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_group(self, Group, index):
        wd = self.application.wd
        self.select_group(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("update").click()
        self.return_to_group()
        self.group_cache = None

    group_cache = None  # создаем переменную, в которую будет записываться текущее кол-во групп (кэш групп)

    # Проверка на соответствие количества групп до и после действия (скрипта)
    def get_group_list(self):
        if self.group_cache is None:  # проверка на наличие записей в массиве с группами
            wd = self.application.wd
            #  Проверка на нахождение на странице с группами
            try:
                wd.find_element_by_name("new")
            except NoSuchElementException:
                self.open_group()
            # Создание массива со списком групп
            self.group_cache = []  # создаем массив для групп
            for element in wd.find_elements_by_css_selector('span.group'):  # перебираем группы в списке групп
                g_name = element.text  # название группы, можно ещё "element.get_attribute('text')"
                id_i = element.find_element_by_name("selected[]").get_attribute('value')  # id группы
                self.group_cache.append(Group(name=g_name, id=id_i))  # добавляем в ранее созданный массив
        return list(self.group_cache)  # возвращаем копию кэша

    def check(self):
        try:
            wd = self.application.wd
            self.open_group()
            wd.find_element_by_name("selected[]")
            return True
        except NoSuchElementException:
            return False

