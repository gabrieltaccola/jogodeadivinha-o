print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numeroseceto = random.randrange(1, 51)
totaldetentativas = 10

chute = input("Digite o seu número: ")
print("Você digitou: ", chute)

chuteNumerico = int(chute)

while(totaldetentativas > 0):
    print("Você tem ", totaldetentativas, " tentativas")
    totaldetentativas = totaldetentativas - 1
    print("tentativa restante: ", totaldetentativas)



acertou = chuteNúmerico == numerosecreto
maior = chuteNúmerico > numerosecreto
menor = chuteNúmerico < numerosecreto

#se você digitar qualquer número vou verificar se acertou ou errou
if(acertou):
    print("Você acertou!Fim de jogo")
else:
    print("Você errou! O seu chute foi maior que o numero secreto")
elif(menor):
    print("Você errou! O seu chute foi maior que o nimero secreto")
print("Fim de jogo")