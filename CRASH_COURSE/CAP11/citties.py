def paises(cidade, pais, populacao=''):
    if populacao:
        return f'A cidade de {cidade.title()} fica no país {pais.title()} e tem uma população de {populacao}.'
    else:
        return f'A cidade de {cidade.title()} fica no país {pais.title()}.'


