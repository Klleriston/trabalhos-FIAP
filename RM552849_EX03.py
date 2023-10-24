#Klleriston Nascimento De Andrade 
#RM 552849

#alunos impares
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES: ") #Pedido do enunciado
contadorDeNotasImpares = 0 #Contador para realizar o calculo da média
for i in range (1, 51, 2): #range de 2 em 2 começando de 1 para para no numero 49
    notasAlunosImpares = int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: ")) #Notas do aluno
    contadorDeNotasImpares += notasAlunosImpares #Soma das notas
mediaAlunosImpares = contadorDeNotasImpares / 25 #Calculo da média
    

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES: ")
contadorDeNotasPares = 0
for i in range (2, 51, 2):
    notasAlunosPares = int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    contadorDeNotasPares += notasAlunosPares
mediaAlunosPares = contadorDeNotasPares / 25

if mediaAlunosPares > mediaAlunosImpares:
    print("A média dos ALUNOS PARES é maior.")
elif mediaAlunosImpares > mediaAlunosPares:
    print("A média do ALUNOS IMPARES é maior.")
else:
    print("A média de ambos os alunos são iguais.")
