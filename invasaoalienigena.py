import sys

import pygame

class InvasaoAlienigena:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e crie recursos do jogo"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            # Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #deixa a tela desenhada mais recente visível
            pygame.display.flip()
            
if __name__ == '__main__':
    # Cria uma instância do jogo e executa o jogo
    ai = InvasaoAlienigena()
    ai.run_game()

