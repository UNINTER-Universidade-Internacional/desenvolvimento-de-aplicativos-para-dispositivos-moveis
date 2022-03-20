# Exercício 1 da apostila - aula 02 

# Desafio:
# Desenvolver um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# Calcular e exibir um valor de desconto e o preço final do produto.


preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%'))

desconto = preco * (p / 100)
final = preco - desconto

print("O preço do produto é {}. Desconto de {}%. ".format(preco, p))
print("Valor Calculado de desconto: {}. Valor final do produto: {}".format(desconto, final))

# Aluno: Luan Henrique Nutels Moraes
# Curso: Desenvolvimento de Aplicativos Para Dispositivos Móveis
# Disciplina: Lógica de programação e Algoritmo.
# @ UNINTER Centro Universitário Internacional.