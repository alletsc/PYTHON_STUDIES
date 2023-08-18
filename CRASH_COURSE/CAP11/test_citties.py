from citties import paises

def test_paises():
    cidade = 'Rio de Janeiro'
    pais = 'Brasil'
    expected_output = f'A cidade de {cidade.title()} fica no país {pais.title()}.'
    assert paises(cidade, pais) == expected_output

def test_paises_populacao():
    cidade = 'Rio de Janeiro'
    pais = 'Brasil'
    populacao = '6.32 milhões'
    expected_output = f'A cidade de {cidade.title()} fica no país {pais.title()} e tem uma população de {populacao}.'
    assert paises(cidade, pais, populacao) == expected_output

