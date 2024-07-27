#Contador de Vogais

frase = input("Digite uma palvara ou uma frase que \n vou contar as vogais:\n ")

contador_vogais = 0 

vogais = "AEIOUaeio"

for letra in frase:
     if letra in vogais: 
          contador_vogais += 1

print("o Números de vogai na string é:", contador_vogais)