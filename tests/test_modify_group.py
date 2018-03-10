from model.group import Group


def test_modify_group(app):
    app.session.Login(username="admin", password="secret")
    app.group_managment.modify_first_group(Group(footer="Bomberman"))
    app.session.Logout()
