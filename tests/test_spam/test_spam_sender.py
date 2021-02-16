import pytest
from unittest.mock import Mock
from victorbaptistalemos_libpythonpro.spam.main import SpamSender
from victorbaptistalemos_libpythonpro.spam.email_sender import EmailSender
from victorbaptistalemos_libpythonpro.spam.user import User


class EmailSenderMock(EmailSender):
    def __init__(self):
        super().__init__()
        self.total_sent = 0
        self.send_parameters = None

    def send(self, send_from, send_to, send_subject, send_message):
        self.total_sent += 1
        self.send_parameters = (send_from, send_to, send_subject, send_message)


@pytest.mark.parametrize(
    'users',
    [
        [
            User('Victor', 'victorbaptistalemos@icloud.com'),
            User('Baptista', 'victorbaptistalemos@gmail.com'),
            User('Lemos', 'victorbaptistalemos@ymail.com')
        ],
        [User('Victor', 'victorbaptistalemos@icloud.com')]
    ]
)
def test_total_spam_sent(session, users):
    for user in users:
        session.add_user(user)
    email_sender = Mock()
    spam_sender = SpamSender(session, email_sender)
    spam_sender.send(
        'victorbaptistalemos@gmail.com',
        'Curso Python Pro, Módulo PyTools',
        'Confira os módulos fantásticos'
    )
    assert len(users) == email_sender.send.call_count


def test_spam_parameters(session):
    user = User('Victor', 'victorbaptistalemos@icloud.com')
    session.add_user(user)
    email_sender = Mock()
    spam_sender = SpamSender(session, email_sender)
    spam_sender.send(
        'victorbaptistalemos@gmail.com',
        'Curso Python Pro, Módulo PyTools',
        'Confira os módulos fantásticos'
    )
    email_sender.send.assert_called_once_with(
        'victorbaptistalemos@gmail.com',
        'victorbaptistalemos@icloud.com',
        'Curso Python Pro, Módulo PyTools',
        'Confira os módulos fantásticos'
    )
