import pygame
from pygame.time import Clock
from cores import *
from fisica import *
from classe_cenario import Cenario

class Pacman:
    def __init__(self, tamanho) -> None:
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha


    def calcularRegras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)


    def pintar(self, tela):
        # Desenha o Pacman
        pygame.draw.circle(tela, yellow, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenho da boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)

        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, dark, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)

        pygame.draw.circle(tela, dark, (olho_x, olho_y), olho_raio, 0)

    
    def processarEventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0


    def processarEventosMouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay


    def aceitarMovimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
