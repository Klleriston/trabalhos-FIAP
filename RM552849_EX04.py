#Klleriston Nascimento De Andrade 
#RM 552849

minutosLocal = int(input("Digite os minutos atuais para liberar a senha: "))

numeroFatorial = 1 #fatorial é igual a 1 pra não zerar a conta
for i in range(1, minutosLocal + 1): #laço de iteração começando pelo 1 pelo mesmo motivo, "minutosLocal + 1" para reazlizar o calculo correto.
    numeroFatorial *= i #realizar calculo

senha = "LIBERDADE" + str(numeroFatorial) #unir o numero em forma de string a senha

print(f"A senha é {senha}")