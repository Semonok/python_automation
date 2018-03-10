
def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group_managment.delete_group()
    app.session.Logout()


