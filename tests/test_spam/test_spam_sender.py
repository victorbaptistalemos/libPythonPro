from victorbaptistalemos_libpythonpro.spam.main import SpamSender
from victorbaptistalemos_libpythonpro.spam.email_sender import EmailSender


def test_spam_sender(session):
    spam_sender = SpamSender(session, EmailSender())
    spam_sender.send(
        'victorbaptistalemos@gmail.com',
        'Curso Python Pro, Módulo PyTools',
        'Confira os módulos fantásticos'
    )