from model.group import Group


def test_modify_group_name(app):
    app.group_managment.modify_first_group(Group(name="Bomb"))


def test_modify_group_header(app):
    app.group_managment.modify_first_group(Group(header="Bomber"))


def test_modify_group_footer(app):
    app.group_managment.modify_first_group(Group(footer="Bomberman"))
