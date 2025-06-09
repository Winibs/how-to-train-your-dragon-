import pygame
import random
import os
import tkinter as tk
from tkinter import messagebox
from adds.adds import inicializarBancoDeDados
from adds.adds import escreverDados
import json

pygame.init()
inicializarBancoDeDados()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("How to train your Dragon")
icon = pygame.display.set_icon(pygame.image.load("assets/icon.jpg"))
white = (255,255,255)
black = (0,0,0)
banguela = pygame.image.load("assets/pngwing.com.png")
startgame = pygame.image.load("assets/startgame.jpg")
backscreen =  pygame.image.load('assets/fundogame.jpg')
DeadScreen = pygame.image.load('assets/dead.jpg')
def mostrar_mensagem(mensagem):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    messagebox.showinfo("Informação", mensagem)
    root.destroy()  # Fecha a janela após exibir a mensagem

