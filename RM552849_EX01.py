#Klleriston Nascimento De Andrade 
#RM 552849
print("-----------------------")
print("Bem vindo ao sistema: ")
print("-----------------------")
while True :
    ##Tela de home do sistema: 
    print("")
    print("-----------------------")
    print("Planos disponivels:")
    print("Nível  |  Porcentagem sobre o faturamento")
    print("Basic - 30%")
    print("Silver - 20%")
    print("Gold - 10%")
    print("Platinum - 5%")
    print("")

    #Input usuario 
    planoUsuario = input("Informe seu plano: ").lower() #caso o usuario queira deixar em CAPS.
    print("-----------------------")

    #implementação da logica para calcular o valor bonus a ser pago:
    match planoUsuario:
        case 'basic':
            faturamento = float(input("Informe seu faturamento anual: "))
            valorBonus = faturamento * 0.3 #calculo
            print(f"Graças ao seu plano ({planoUsuario}) o valor a ser pago é de R$:{valorBonus:.2f}")
        case 'silver':
            faturamento = float(input("Informe seu faturamento anual: "))
            valorBonus = faturamento * 0.2
            print(f"Graças ao seu plano ({planoUsuario}) o valor a ser pago é de R$:{valorBonus:.2f}")
        case 'gold':
            faturamento = float(input("Informe seu faturamento anual: "))
            valorBonus = faturamento * 0.1
            print(f"Graças ao seu plano ({planoUsuario}) o valor a ser pago é de R$:{valorBonus:.2f}")
        case 'platinum':
            faturamento = float(input("Informe seu faturamento anual: "))
            valorBonus = faturamento * 0.05
            print(f"Graças ao seu plano ({planoUsuario}) o valor a ser pago é de R$:{valorBonus:.2f}")
        case _:
            print(f"Por favor insira um valor valido.") 
    
    #Logica para finalizar o programa: 
    print("Deseja encerrar o programa: [y] or [n]")
    escolha = input("").lower().startswith("y")
    if escolha is True:
        print("Obrigado por usar nosso sistema !!")
        break
    