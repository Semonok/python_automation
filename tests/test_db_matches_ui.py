from model.group import Group


def test_matches_db_and_ui(app, db):
    groups_ui = app.group_managment.get_group_list()
    def clean(group):
        return Group(id=group.id,name=group.name.strip())
    groups_db = map(clean, db.get_group_list())
    assert sorted(groups_ui, key=Group.id_or_max) == sorted(groups_db, key=Group.id_or_max)