import pygame
from pygame.constants import QUIT
from classe_pacman import Pacman
from classe_fantasma import Fantasma
from cores import *
from classe_elemento_jogo import ElementoJogo
from elementos import *
import random

class Cenario(ElementoJogo):
    def __init__(self, tamanho, pac) -> None:
        self.pacman = pac
        self.moviveis = []
        self.tamanho = tamanho
        self.pontos = 0
        # Estados: 0 = Jogando, 1 = Pausado, 2 = GameOver, 3 = Vitória
        self.estado = 0
        self.vidas = 3
        self.matriz = MATRIZ


    def adicionarMovivel(self, obj):
        self.moviveis.append(obj)


    def getDirecoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(pCima)
        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(pBaixo)
        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(pEsquera)
        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(pDireita)
        return direcoes

    # Score
    def pintarScore(self, tela):
        fonte = pygame.font.SysFont("sans", 28, True, False)
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render(f"Score: {self.pontos}", True, yellow)
        img_vidas = fonte.render(f"Vidas: {self.vidas}", True, yellow)
        tela.blit(img_pontos, (pontos_x, 50))
        tela.blit(img_vidas, (pontos_x, 100))


    def pintarLinha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = dark
            if coluna == 2:
                cor = blue
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, yellow, (x + half, y + half), self.tamanho // 10, 0)
            if coluna == 3:
                pygame.draw.circle(tela, red, (x + half, y + half), self.tamanho // 5, 0)
            if coluna == 4:
                pygame.draw.circle(tela, green, (x + half, y + half), self.tamanho // 5, 0)

    # Pinta os estados do jogo
    def pintar(self, tela):
        if self.estado == 0:
            self.pintarJogando(tela)
        elif self.estado == 1:
            self.pintarJogando(tela)
            self.pintarPausado(tela)
        elif self.estado == 2:
            self.pintarJogando(tela)
            self.pintarGameOver(tela)
        elif self.estado == 3:
            self.pintarJogando(tela)
            self.pintarVitoria(tela)

    # Função para adicionar texto
    def pintarTexto(self, tela, texto):
        fonte = pygame.font.SysFont("sans", 28, True, False)
        imgTexto = fonte.render(texto, True, white)
        texto_x = (tela.get_width() - imgTexto.get_width()) // 2
        texto_y = (tela.get_width() - imgTexto.get_height()) // 2
        tela.blit(imgTexto, (texto_x, texto_y))


    def pintarPausado(self, tela):
        self.pintarTexto(tela, "PAUSADO")


    def pintarJogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintarLinha(tela, numero_linha, linha)
        self.pintarScore(tela)


    def pintarGameOver(self, tela):
        self.pintarTexto(tela, "GAME OVER")


    def pintarVitoria(self, tela):
        self.pintarTexto(tela, "VOCÊ GANHOU!")

    
    def calcularRegras(self):
        if self.estado == 0:
            self.calcularRegrasJogando()
        elif self.estado == 1:
            self.calcularRegrasPausado()
        elif self.estado == 2:
            self.calcularRegrasGameOver()


    def calcularRegrasJogando(self):
        for movivel in self.moviveis:
            lin = int(movivel.linha)
            col = int(movivel.coluna)
            lin_intencao = int(movivel.linha_intencao)
            col_intencao = int(movivel.coluna_intencao)
            direcoes = self.getDirecoes(lin, col)
            if len(direcoes) >= 3:
                movivel.esquina(direcoes)

            if isinstance(movivel, Fantasma) and movivel.linha == self.pacman.linha and movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                if self.vidas <= 0:
                    self.estado = 2
                else:
                    clinha = [1.0, 27.0]
                    ccoluna = [1.0, 26.0]
                    self.pacman.linha = random.choice(clinha)
                    self.pacman.coluna = random.choice(ccoluna)

            else:
                if 0 <= col_intencao <= 27 and 0 <= lin_intencao <= 28:
                    if self.matriz[lin_intencao][col_intencao] != 2:
                        movivel.aceitarMovimento()
                        if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1:
                            self.pontos += 1
                            self.matriz[lin][col] = 0
                            if self.pontos >= 306:
                                self.estado = 3
                        if isinstance(movivel, Pacman) and self.matriz[lin][col] == 3:
                            self.pontos += 1
                            self.matriz[lin][col] = 0
                            self.vidas += 1
                        if isinstance(movivel, Pacman) and self.matriz[lin][col] == 4:
                            self.pontos += 1
                            self.matriz[lin][col] = 0
                    else:
                        movivel.recusarMovimento(direcoes)


    def calcularRegrasPausado(self):
        pass


    def calcularRegrasGameOver(self):
        pass


    def processarEventos(self, eventos):
        for e in eventos:
            if e.type == QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado == 0:
                        self.estado = 1
                    else:
                        self.estado = 0
