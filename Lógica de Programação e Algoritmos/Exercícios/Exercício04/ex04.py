# Exercício 4 da apostila - aula 03

# Desafio:
# Exercício de condicional simples, traduzir as afirmações a seguir para condicionais em Python:

# a) Se idade é maior que 60, escreva: "Você tem direitos aos benefícios" 

if (idade > 60):
print('Você tem direito aos benefícios')
  
# b) Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!

if (dano > 10 and escudo == 0):
print('Você está morto!')

# c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"

#Exemplo 1
if (norte == True or sul == True or leste == True or oeste == True):
print('Você escapou!')

#Exemplo 2 
#Equivalente a expressão anterior. 
if (norte or sul or leste or oeste):
print('Você escapou!')


# Aluno: Luan Henrique Nutels Moraes
# Curso: Desenvolvimento de Aplicativos Para Dispositivos Móveis
# Disciplina: Lógica de programação e Algoritmo
# @ UNINTER Centro Universitário Internacional.