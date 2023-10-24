import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['fczanetti@hotmail.com', 'foo@bar.com.br'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'fzanettifa@gmail.com',
        'Cursos Python Pro',
        'Primeira turma aberta'
    )
    assert remetente in resultado
# Neste teste poderia ser usado um for, onde para cada destinatário em uma lista de destinatário seria executado um
# teste e um assert. Porém no primeiro erro o teste iria parar, não executando os itens do restante da lista. Portanto
# a solução é usar o @pytest.mark.parametrize, que executa os testes para todos os itens da lista declarada e informa
# quantos falharam e quantos passaram.


@pytest.mark.parametrize('remetente', ['', 'fabio'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'fzanettifa@gmail.com',
            'Cursos Python Pro',
            'Primeira turma aberta'
        )
