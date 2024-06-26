import random

# definindo a função do jogo da forca
def jogo_da_forca():
    frases = [
        "BORA FICAR DE CONCHINHA",
        "NAMORA COMIGO",
        "NOS DOIS E UM GATINHO",
        "EU E TU JUNTOS",
        "BE MINE"
    ]
    
    # escolhe as frases aleatoriamente
    frase = random.choice(frases)
    adivinhados = ["_" if letra != " " else " " for letra in frase]
    tentativas = len(frase) + 10  # Dá tentativas extras para a ocasião especial
    letras_adivinhadas = set()

    print("Jogo da Forca Especial!")
    print("Descubra a frase e tenha uma surpresa...")

    while tentativas > 0 and "_" in adivinhados:
        print(f"\n{' '.join(adivinhados)}")
        print(f"Tentativas restantes: {tentativas}")
        palpite = input("Digite uma letra ou a frase: ").upper()

        if len(palpite) == 1 and palpite.isalpha():
            if palpite in letras_adivinhadas:
                print("Você já tentou essa letra.")
            elif palpite not in frase:
                print("Errado!")
                tentativas -= 1
            else:
                print("Certo!")
                for indice, letra in enumerate(frase):
                    if letra == palpite:
                        adivinhados[indice] = palpite
            letras_adivinhadas.add(palpite)
        elif palpite == frase:
            print("Parabéns! Você descobriu a frase!")
            break
        else:
            print("Tenta de novo aí.")
            tentativas -= 1

    if "_" not in adivinhados:
        print(f"\nA frase era: {''.join(adivinhados)}")
        print("Boaa, acertou! \nEai, topas? <3")
    else:
        print("\nPoxa, acabaram as tentativas. \nMas o pedido ainda está de pé hein! :D")

# chamando a função pra iniciar o joguin
jogo_da_forca()
