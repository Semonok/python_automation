from model.group import Group


def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group_managment.open_group()
    app.group_managment.Create_new_group(Group(name="123", header="321", footer="195"))
    app.group_managment.return_to_group()
    app.session.Logout()
