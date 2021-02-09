from victorbaptistalemos_libpythonpro.spam.user import User


def test_add_users(session):
    user = User(name='Victor')
    session.add_user(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Victor'), User(name='Baptista'), User(name='Lemos')]
    for user in users:
        session.add_user(user)
    assert users == session.list_users()
