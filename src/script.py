import json as j
import os
import sys
from time import sleep

import pyautogui as pp

#função para pegar o caminho do recurso
def caminho_recurso(nome):
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base, "src", nome)


with open(caminho_recurso("banco.json"), "r", encoding="utf-8") as arquivo:
    dados = j.load(arquivo)

# Função para iniciar o programa
def iniciar_programa():
    pp.hotkey("ctrl", "esc")
    sleep(1)

    pp.write("microsoft edge")
    sleep(1)

    pp.press("enter")
    sleep(1)

    for i in dados:
        pp.write(str(i), interval=0.1)
        sleep(0.5)
        pp.press("enter")
        sleep(5)

        pp.press("q")
        sleep(0.25)

        pp.hotkey("ctrl", "a")
        sleep(0.25)

        pp.press("backspace")
        sleep(0.25)