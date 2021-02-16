from unittest.mock import Mock

import pytest

from victorbaptistalemos_libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    # Cria uma classe substituta
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/52052351?v=4'
    # Adiciona um método json que retorna um dicionário
    resp_mock.json.return_value = {
        "login": "victorbaptistalemos",
        "id": 52052351,
        "avatar_url": "https://avatars.githubusercontent.com/u/52052351?v=4",
        "url": "https://api.github.com/users/victorbaptistalemos"
    }
    # Utiliza a lib pytest-mock para controlar a assinatura do método
    get_mock = mocker.patch('victorbaptistalemos_libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('victorbaptistalemos')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('victorbaptistalemos')
    assert url == 'https://avatars.githubusercontent.com/u/52052351?v=4'
