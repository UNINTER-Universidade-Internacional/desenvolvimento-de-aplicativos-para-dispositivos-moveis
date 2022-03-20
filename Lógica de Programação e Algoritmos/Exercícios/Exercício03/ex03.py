# Exercício 3 da apostila - aula 02 

# Desafio:
# Criar uma variável de string que receba uma frase qualquer. Criar uma segunda variável, agora contendo a metade da string digitada.
# Imprimir na tela somente os dois últimos caracters da segunda variável do tipo string. 


frase = input('Digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:])

# Aluno: Luan Henrique Nutels Moraes
# Curso: Desenvolvimento de Aplicativos Para Dispositivos Móveis
# Disciplina: Lógica de programação e Algoritmo
# @ UNINTER Centro Universitário Internacional.