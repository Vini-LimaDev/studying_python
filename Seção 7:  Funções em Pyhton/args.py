"""
Entendendo *args 

- o *args é um parametro como qualqeruer outro, isso significa que voce pode chamar de qualquer coisa, desde que comece com asterisco.

exemplo:
*x

Mas por convenção chamamos de *args

Mas o que é o *args?
O parametro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

"""
def soma_todos_numeros(*args):
    return sum(args)    

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))          
print(soma_todos_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Logo, sempre que utilizamos o *args, podemos passar n parametros para a função