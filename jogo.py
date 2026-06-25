print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numeroseceto= 40

chute = input("Digite o seu número: ")
print("Você digitou: ", chute)

chuteNúmerico = int(chute)

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