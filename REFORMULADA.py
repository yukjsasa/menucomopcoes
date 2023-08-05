imposto = 0
salario = 0
novosal = 0
escolha =  0
finalizou = True


while finalizou:
     
 print('Seja Bem-Vindo ao Programa!')

 print('Menu de Opções:')
 print(' 1 - imposto')
 print(' 2 - Novo salário')
 print(' 3 - Finalizar o programa')
 escolha = int(input('digite sua escolha:'))
 

 if escolha == 1:
     
     salario = int(input('Digite seu salário:'))
     if salario < 500:
      imposto = salario * 5 / 100
      print('seu imposto é:', imposto, "Reais")
     elif salario >= 500 or salario <=850:
      imposto = salario * 10 /100
      print('seu imposto é:', imposto, "Reais")
     else:
      imposto = salario * 15 / 100
      print('seu imposto é:', imposto, "Reais")
 
 if escolha == 2:
    
    salario = int(input('Digite seu salário:'))
    if salario > 1500:
      novosal = salario + 25
      print('seu novo salario é:', novosal)
    elif salario >= 750 and salario < 1500:
      novosal = salario + 50
      print('seu novo salario é:', novosal)
    elif salario >= 450 and salario < 750:
      novosal = salario + 75
      print('seu novo salario é:', novosal)
    else:
      novosal = salario + 100
      print('seu novo salario é:', novosal)
    
 if escolha == 3:
    finalizou = False
    print('Programa Encerrado!!!')



