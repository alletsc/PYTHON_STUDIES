from TESTES_COM_PYTHON.codigo.jogo import brincadeira

"""
O teste é formado por três partes:
Given: onde você prepara o cenário de teste - dado
When: onde você executa o código que será testado - quando
Then: onde você verifica se o resultado é o esperado - entao
"""

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    valor_entrada = 1
    valor_esperado = 1
    valor_retornado = brincadeira(valor_entrada)
    assert valor_retornado == valor_esperado
