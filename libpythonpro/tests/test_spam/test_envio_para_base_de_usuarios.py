from unittest.mock import Mock

import pytest
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Fabio', email='fczanetti@hotmail.com'),
            Usuario(nome='Fernanda', email='fernanda@hotmail.com')
        ],
        [
            Usuario(nome='Fabio', email='fczanetti@hotmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fczanetti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Fabio', email='fczanetti@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fernanda@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
    enviador.enviar.assert_called_once_with(
        'fernanda@hotmail.com',
        'fczanetti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
