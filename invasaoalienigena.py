import sys

import pygame

from configuracoes import Configuracoes 

class InvasaoAlienigena:

    """Classe geral para gerenciar ativos e comportamento do jogo"""
    def __init__(self):

        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.configuracoes = Configuracoes()

        self.screen = pygame.display.set_mode(
            (self.configuracoes.screen_width, self.configuracoes.screen_height))

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):

        """Inicia o loop principal do jogo"""
        while True:

            # Observa eventos de teclado e mouse
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    sys.exit()

            #Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.configuracoes.bg_color)

            #deixa a tela desenhada mais recente visível
            pygame.display.flip()

            self.clock.tick(60)

            
if __name__ == '__main__':

    # Cria uma instância do jogo e executa o jogo

    ai = InvasaoAlienigena()
    ai.run_game()

