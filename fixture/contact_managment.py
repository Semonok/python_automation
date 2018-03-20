from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    # Для выборочного заполнения полей контакта:
    # (если при вызове метода 'contact' определяем значения атрибута, тогда заполняем)
    def change_field_value(self, field_name, text_name):
        wd = self.app.wd
        if text_name is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text_name)

    contact_cache = None  # создаем переменную, в которую будет записываться текущее кол-во групп (кэш групп)

    # Создание списка групп (для проверок колчиства групп до и после операциий с ними)
    def get_contact_list(self):
        if self.contact_cache is None:  # проверка на наличие записей в массиве с группами
            wd = self.app.wd
            self.app.open_home_page()
            # Создание массива со списком контактов
            self.contact_cache = []  # создаем массив для контактов
            for element in wd.find_elements_by_name('entry'):  # перебираем контакты в списке контактов
                cell = element.find_elements_by_tag_name("td")
                name = cell[1].text  # имя контакта
                last = cell[2].text  # фамилия контакта
                id_i = cell[0].find_element_by_tag_name("input").get_attribute('value')  # id контакта
                all_phones = cell[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=name, lastname=last, id=id_i,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))  # добавляем в ранее созданный массив
        return list(self.contact_cache)  # возвращаем копию кэша

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(firstname, lastname, homephone, mobilephone, workphone, secondaryphone, id)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        info = wd.find_element_by_id("content").text
        homephone = re.search('H: (.*)', info).group(1)
        mobilephone = re.search('M: (.*)', info).group(1)
        workphone = re.search('W: (.*)', info).group(1)
        secondaryphone = re.search('P: (.*)', info).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name('entry')[index]
        cell = element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name('entry')[index]
        cell = element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
