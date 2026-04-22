import pytest
from exemplo_aula.pessoa import Pessoa


@pytest.mark.parametrize(
    "nome, idade",
    [
        ("nelson", 21),
        ("ana", 21),
    ]
)
def test_pessoa(nome, idade):
    pessoa = Pessoa(nome, idade)
    
    assert pessoa.nome == nome
    assert pessoa.idade == idade

@pytest.mark.parametrize(
    "nome, idade",
    [
        ("nelson", "21"),
        (21, 21)
    ]
)
def test_pessoa_exception(nome,idade):
    with pytest.raises(Exception):
        Pessoa(nome,idade)
        