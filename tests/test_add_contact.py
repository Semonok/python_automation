from model.contact import Contact


def test_add_contact_pro(app):
    contact_new = Contact(lastname='Petrov', firstname='Vasya', mobilephone=79856326458)
    old_list = app.contact_managment.get_contact_list()
    app.contact_managment.add_contact(contact_new)
    new_list = app.contact_managment.get_contact_list()  # длина группы после добавления
    assert len(old_list) + 1 == len(new_list)  # сравниваем кол-во групп до и после добавления группы
    # Создаем проверку элементов контакта
    old_list.append(contact_new)  # Добавляем в старый список групп, новую группу (это нужно только для проверки)
    assert sorted(old_list, key=Contact.id_or_max) == sorted(new_list, key=Contact.id_or_max)  # Сортируем по ключу при сравнении