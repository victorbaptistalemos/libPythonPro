import pytest

from victorbaptistalemos_libpythonpro.spam.db import Connection


@pytest.fixture(scope='session')
def connection():
    # Setup
    connection_obj = Connection()
    yield connection_obj
    # Tear Down
    connection_obj.close()


@pytest.fixture
def session(connection):
    # Setup
    session_obj = connection.get_session()
    yield session_obj
    # Tear Down
    session_obj.roll_back()
    session_obj.close()
