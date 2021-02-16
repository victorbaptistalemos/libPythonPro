from victorbaptistalemos_libpythonpro.spam.user import User


def test_add_users(session):
    user = User('Victor', 'victorbaptistalemos@icloud.com')
    session.add_user(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [
        User('Victor', 'victorbaptistalemos@icloud.com'),
        User('Baptista', 'victorbaptistalemos@gmail.com'),
        User('Lemos', 'victorbaptistalemos@ymail.com')
    ]
    for user in users:
        session.add_user(user)
    assert users == session.list_users()
