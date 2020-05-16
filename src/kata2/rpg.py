#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    # Valores validos para una contraseña
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    password = ""

    # Agregamos caracteres aletorios, a partir de valores.
    password = password.join([random.choice(valores) for i in range(passLen)])

    return password
