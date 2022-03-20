# Exercício 5 da apostila - aula 03

# Desafio:
# Criar um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verificar se os valores formam um triângulo e classificar como:
# Observação: Lembrar de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois (Exercícios da apostila - aula 03)

# a) Equilátero (três lados iguais)
# b) Isóceles (dois lados iguais)
# c) Escaleno (três lados diferentes)

A = int(input('Digite o primeiro lado do triângulo:'))
B = int(input('Digite o segundo lado do triângulo:'))
C = int(input('Digite o terceiro lado do triângulo:'))

# Validação 

if (A > 0) and (B > 0) and (C > 0): 
   if (A + B > C) and (A + C > B) and (B + C > A):
   # Se o programa chegou até aqui, é porque o triangulo é válido!
      if A != B and A != C and B != C:
         print('Triangulo escaleno!')
       else:
           if A == B and A == C and B == C:
                print('Triangulo equilátero!')
              else:
                print('Triangulo isósceles!')
            
else:
     print('Ao menos um dos valores indicados não servem para formar um triângulo')   
   else:
      print('Ao menos um dos valores indicados não servem para formar um triângulo')


# Aluno: Luan Henrique Nutels Moraes
# Curso: Desenvolvimento de Aplicativos Para Dispositivos Móveis
# Disciplina: Lógica de programação e Algoritmo
# @ UNINTER Centro Universitário Internacional.