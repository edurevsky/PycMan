import pygame
import random
from classe_movivel import Movivel
from classe_elemento_jogo import ElementoJogo
from cores import *
from elementos import *


class Fantasma(ElementoJogo, Movivel):
    def __init__(self, cor, tamanho):
        self.coluna = 13.0
        self.linha = 15.0
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = pBaixo
        self.tamanho = tamanho
        self.cor = cor


    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py +self.tamanho)]

        pygame.draw.polygon(tela, self.cor, contorno, 0)

        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_e_x = int(px + fatia * 2.5)
        olho_e_y = int(py + fatia * 2.5)

        olho_d_x = int(px + fatia * 5.5)
        olho_d_y = int(py + fatia * 2.5)

        pygame.draw.circle(tela, white, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, dark, (olho_e_x - 1, olho_e_y), olho_raio_int, 0)
        pygame.draw.circle(tela, white, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, dark, (olho_d_x - 1, olho_d_y), olho_raio_int, 0)

        
    def calcularRegras(self):
        if self.direcao == pCima:
            self.linha_intencao -= self.velocidade
        if self.direcao == pBaixo:
            self.linha_intencao += self.velocidade
        if self.direcao == pEsquera:
            self.coluna_intencao -= self.velocidade
        if self.direcao == pDireita:
            self.coluna_intencao += self.velocidade


    def mudarDirecao(self, direcoes):
        self.direcao = random.choice(direcoes)


    def esquina(self, direcoes):
        self.mudarDirecao(direcoes)


    def aceitarMovimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao


    def recusarMovimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudarDirecao(direcoes)


    def processarEventos(self, eventos):
        pass

