from unittest.mock import Mock

import pytest

from victorbaptistalemos_libpythonpro import github_api


@pytest.fixture
def avatar_url():
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
    # Setup
    # Separa o método get em uma variável
    get_github_api = github_api.requests.get
    # Depois altera o método get recebendo uma classe substituta
    # Dessa forma o teste não depende mais de internet para funcionar
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('victorbaptistalemos')
    yield url
    # Tier Down
    # Depois do teste retorna o método get a sua asssinatura original
    github_api.requests.get = get_github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('victorbaptistalemos')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('victorbaptistalemos')
    assert url == 'https://avatars.githubusercontent.com/u/52052351?v=4'
