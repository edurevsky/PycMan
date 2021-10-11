import pygame
from classe_cenario import *
from classe_pacman import *
from classe_fantasma import *
from elementos import *
from cores import *

class App:
    def run():
        pygame.init()

        pygame.display.set_caption("PycMan")
        window = pygame.display.set_mode((800, 600), 0)

        if __name__ == "__main__":
                pacman = Pacman(SIZE)
                blinky = Fantasma(red, SIZE)
                inky = Fantasma(cian, SIZE)
                clyde = Fantasma(orange, SIZE)
                pinky = Fantasma(pink, SIZE)
                cenario = Cenario(SIZE, pacman)
                cenario.adicionarMovivel(pacman)
                cenario.adicionarMovivel(blinky)
                cenario.adicionarMovivel(inky)
                cenario.adicionarMovivel(clyde)
                cenario.adicionarMovivel(pinky)

                while True:
                    # Calcular regras
                    cenario.calcularRegras()
                    pacman.calcularRegras()
                    blinky.calcularRegras()
                    inky.calcularRegras()
                    clyde.calcularRegras()
                    pinky.calcularRegras()

                    # Pintar a tela
                    window.fill(dark)
                    cenario.pintar(window)
                    pacman.pintar(window)
                    blinky.pintar(window)
                    inky.pintar(window)
                    clyde.pintar(window)
                    pinky.pintar(window)
                    pygame.display.update()

                    fps = pygame.time.Clock()
                    fps.tick(16)

                    # Captura eventos
                    eventos = pygame.event.get()
                    pacman.processarEventos(eventos)
                    cenario.processarEventos(eventos)


if (__name__ == "__main__"):
    App.run()
