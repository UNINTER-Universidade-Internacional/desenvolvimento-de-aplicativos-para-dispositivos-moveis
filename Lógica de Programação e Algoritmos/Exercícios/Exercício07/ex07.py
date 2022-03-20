# Exercício 7 da apostila - aula 03

# Desafio:
# Escrever um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Perguntar a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
      
        
kwh = float(input('Quantos kwh?'))
tipo = input('Qual o tipo de instalação (R, C ou I)')

if (tipo == 'R'):
       if kwh <= 500:
           preco = 0.4   
       else:
              preco = 0.65
       
elif (tipo == 'C'):
       if kwh <= 1000:
           preco = 0.55
       else:
              preco = 0.6
       
elif (tipo == 'I'):
       if kwh <= 5000:
           preco = 0.55 
       else:
           preco = 0.6
       
else:
    print('Instalação inválida!')
    
print('Total a pagar: {}'.format(kwh * preco))
       


# Aluno: Luan Henrique Nutels Moraes
# Curso: Desenvolvimento de Aplicativos Para Dispositivos Móveis
# Disciplina: Lógica de programação e Algoritmo
# @ UNINTER Centro Universitário Internacional.