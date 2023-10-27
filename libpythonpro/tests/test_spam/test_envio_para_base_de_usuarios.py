import pytest
from libpythonpro.spam.enviador_de_email import Enviador
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fczanetti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
    assert len(usuarios) == enviador.qtd_emails_enviados
