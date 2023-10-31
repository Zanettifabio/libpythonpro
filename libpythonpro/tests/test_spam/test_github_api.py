from unittest.mock import Mock
from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {'login': 'Zanettifabio', 'id': 140400945, 'node_id': 'U_kgDOCF5ZMQ',
                                   'avatar_url': 'https://avatars.githubusercontent.com/u/140400945?v=4'}
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Zanettifabio')
    assert 'https://avatars.githubusercontent.com/u/140400945?v=4' == url
