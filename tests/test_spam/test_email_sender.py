import pytest

from victorbaptistalemos_libpythonpro.spam.email_sender import EmailSender, InvalidEmail


def test_sending_mail():
    email_sender = EmailSender()
    assert email_sender is not None


@pytest.mark.parametrize(
    'send_from',
    [
        'victorbaptistalemos@icloud.com',
        'victorbaptistalemos@gmail.com',
        'victorbaptistalemos@ymail.com'
    ]
)
def test_send_from(send_from):
    email_sender = EmailSender()
    sender = email_sender.send(
        send_from,
        'victorbaptistalemos@icloud.com',
        'Teste de envio de e-mail',
        'Testando envio de e-mail.'
    )
    assert send_from in sender


@pytest.mark.parametrize(
    'send_from',
    [
        '',
        'victorbaptistalemos'
    ]
)
def test_invalid_send_from(send_from):
    email_sender = EmailSender()
    with pytest.raises(InvalidEmail):
        sender = email_sender.send(
            send_from,
            'victorbaptistalemos@icloud.com',
            'Teste de envio de e-mail',
            'Testando envio de e-mail.'
        )
