from victorbaptistalemos_libpythonpro.github_api import buscar_avatar


def test_buscar_avatar():
    assert buscar_avatar('victorbaptistalemos') == 'https://avatars.githubusercontent.com/u/52052351?v=4'
