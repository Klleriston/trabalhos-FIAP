#Klleriston Nascimento De Andrade 
#RM 552849

diasDaSemana = {"segunda-feira":0, "terça-feira":0, "quarta-feira":0, "quinta-feira":0, "sexta-feira":0} #Dicionario para contagem dos votos
votosNoDia = 0; #Contador zerado para qualquer valor ser maior do que ele.
diaMaisVotado = [] #Array de dias mais votados caso haja empate

for dia in diasDaSemana:  #Iteração entre os dias para perguntar o voto do usuario
    votoUsuario = int(input(f"Digite quantos votos foram atribuidos a {dia}: "))
    #Logica para atribuição da notas e substituição de dias.
    diasDaSemana[dia] = votoUsuario
    if votoUsuario > votosNoDia:
        votosNoDia = votoUsuario
        diaMaisVotado = [dia]
    elif votoUsuario == votosNoDia:
        diaMaisVotado.append(dia)
    
if len(diaMaisVotado) == 1: #Se o tamanho do array "diaMaisVotado" for apenas 1, então não houve empate e há um dia mais votado
    print(f"O dia mais votado foi {diaMaisVotado[0]}")
else:  #Case o array tenha mais de um elemento ira exibir os elentos
    print(f"Houve um empate entre os seguintes dias:")
    for dia in diaMaisVotado:
        print(f"{dia}")