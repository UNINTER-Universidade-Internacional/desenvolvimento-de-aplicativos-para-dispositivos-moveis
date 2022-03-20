# Exercício 6 da apostila - aula 03

# Desafio:
# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada (exercício da apostila - aula 3).

print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input("Digite o primeiro valor:"))
    y = int(input("Digite o segundo valor:"))

if (op == '+'):
       res = x + y
       print('Resultado: {} + {} = {}'. format(x, y, res))
       
elif (op == '-'):
       res = x - y
       print('Resultado: {} - {} = {}'. format(x, y, res))
       
elif (op == '*'):
       res = x * y
       print('Resultado: {} * {} = {}'. format(x, y, res))
       
elif (op == '/'):
       res = x / y
       print('Resultado: {} / {} = {}'. format(x, y, res))
       
print('Opereção invalida. ')
print('Encerrando o programa...')

  
  

# Aluno: Luan Henrique Nutels Moraes
# Curso: Desenvolvimento de Aplicativos Para Dispositivos Móveis
# Disciplina: Lógica de programação e Algoritmo
# @ UNINTER Centro Universitário Internacional.