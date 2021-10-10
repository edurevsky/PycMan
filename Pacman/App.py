import pygame
from classe_cenario import *
from classe_pacman import *
from fisica import *
from cores import dark

class App:
    def run():
        pygame.init()

        window = pygame.display.set_mode((800, 580), 0)

        if __name__ == "__main__":
                pacman = Pacman(SIZE)
                cenario = Cenario(SIZE, pacman)

                while True:
                    # Calcular regras
                    pacman.calcularRegras()
                    cenario.calcularRegras()

                    # Pintar a tela
                    window.fill(dark)
                    cenario.pintar(window)
                    pacman.pintar(window)
                    pygame.display.update()

                    fps = pygame.time.Clock()
                    fps.tick(16)

                    # Captura eventos
                    eventos = pygame.event.get()
                    for e in eventos:
                        if e.type == pygame.QUIT:
                            exit()
                    pacman.processarEventos(eventos)

if (__name__ == "__main__"):
    App.run()
