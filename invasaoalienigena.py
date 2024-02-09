import sys
import pygame
from configuracoes import Configuracoes
from ship import Ship

class InvasaoAlienigena:

    """Classe geral para gerenciar ativos e comportamento do jogo"""
    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.configuracoes = Configuracoes()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.configuracoes.screen_width = self.screen.get_rect().width
        self.configuracoes.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()  
            self.clock.tick(60)

    def _check_events(self):
        """Responde as teclas pressionadas e a eventos de mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a teclas pressionadas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde a teclas soltas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False




    def _update_screen(self):
        """Atualiza as imagens na tela e muda para a nova tela"""
        self.screen.fill(self.configuracoes.bg_color)
        self.ship.blitme()

        pygame.display.flip()


            
if __name__ == '__main__':

    # Cria uma instância do jogo e executa o jogo

    ai = InvasaoAlienigena()
    ai.run_game()

