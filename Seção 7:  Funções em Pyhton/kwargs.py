"""
Entendendo o Kwargs
- o **kwargs é um parametro como qualqeruer outro, isso significa que voce pode chamar de qualquer coisa, desde que comece com dois asteriscos.
exemplo:
**x

Mas por convenção chamamos de **kwargs

Mas o que é o **kwargs?
O parametro **kwargs utilizado em uma função, coloca os valores extras informados como entrada em um dicionario. Então desde já lembre-se que dicionarios são mutaveis.

"""

def mostra_nomes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
mostra_nomes(nome="Vinicius", sobrenome="Lima")
mostra_nomes(nome="João", sobrenome="Moreira", idade=30)
mostra_nomes(nome="Ana", sobrenome="Silva", idade=25, cidade="São Paulo")

# Logo, sempre que utilizamos o **kwargs, podemos passar n parametros para a função