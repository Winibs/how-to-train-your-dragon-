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
tamanho = (1000,700)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("How to train your Dragon")
icon = pygame.display.set_icon(pygame.image.load("assets/icon.jpg"))
banguela = pygame.image.load("assets/bangs.png")
startgame = pygame.image.load("assets/StartScreen.jpg")
telaInicio =  pygame.image.load('assets/Fundojogo.jpg')
D_screen = pygame.image.load('assets/lose.jpg')
Menu = pygame.font.SysFont('comicsans',18)
Morte = pygame.font.SysFont('arial',120)
white = (255,255,255)
black = (0,0,0)



def jogar():
    largura_janela = 300
    altura_janela = 50 
    def obter_nome():
        global nome
        nome = entry_nome.get()
        if not nome: 
            messagebox.showwarning('Aviso', 'Por favor, insira um nome.')
            return 
        else:
            print (f'Nome inserido: {nome}')
            root.destroy()
             



    root = tk.Tk()
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    root.title("Insira seu nome")
    root.protocol("WM_DELETE_WINDOW", obter_nome)




    entry_nome = tk.Entry(root)
    entry_nome.pack()

    botao = tk.Button(root, text = "Enviar", command=obter_nome)
    botao.pack()

    root.mainloop()

    
    largura_personagem = 50
    altura_personagem = 50
    posicaoX= 10 
    posicaoY= 275  
    velocidade = 5
    movimento_y = 0

    while True :
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movimento_y = -velocidade
                elif evento.key == pygame.K_DOWN:
                    movimento_y= velocidade


            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    movimento_y = 0


        posicaoY += movimento_y

        if posicaoY < 0:
            posicaoY = 0
        elif posicaoY > tamanho [1] - altura_personagem:
            posicaoY = tamanho[1] - altura_personagem



        tela.fill(white)
        tela.blit(startgame, (0, 0))
        tela.blit(banguela, (posicaoX, posicaoY))
        pygame.display.update()
        relogio.tick(60)
            







        


    
jogar()

