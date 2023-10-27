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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fczanetti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
    assert len(usuarios) == enviador.qtd_emails_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        self.parametros_de_envio = None
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Fabio', email='fczanetti@hotmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fernanda@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
    assert enviador.parametros_de_envio == (
        'fernanda@hotmail.com',
        'fczanetti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos')
