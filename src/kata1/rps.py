from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'

def quienGana(player, ai):
    player = player[0].upper() + player[1:].lower()
    ai = ai[0].upper() + ai[1:].lower()
    print(player, ai)
    if (player == ai):
        return 'Empate!'
    else:
        if (player == options[0] and ai == options[1]):
            return 'Perdiste!'
        elif (player == options[1] and ai == options[2]):
            return 'Perdiste!'
        elif (player == options[2] and ai == options[0]):
            return 'Perdiste!'
        else:
            return 'Ganaste!'

# Entry Point
def Game():
    print("Piedra, Papel o Tijera!")
    player = input("Ingresa una opcion: ")

    ai = options[randint(0,2)]
    
    winner = quienGana(player, ai)

    print(winner)
