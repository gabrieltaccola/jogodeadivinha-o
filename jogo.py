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
if(numeroseceto == chuteNumerico):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim de jogo")