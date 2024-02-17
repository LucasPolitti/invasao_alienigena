import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe para gerenciar os projéteis disparados da espaçonave"""

    def __init__(self, ai_game):
        """Cria um objeto bullet na posição atual da espaçonave"""
        super().__init__()
        self.screen = ai_game.screen
        self.configuracoes = ai_game.configuracoes
        self.color = self.configuracoes.bullet_color

        #Cria um bullet rect em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, self.configuracoes.bullet_width,
                                self.configuracoes.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Armazena a posição do projétil como um float
        self.y = float(self.rect.y)

    def update(self):
        """Desloca o projétil veritcalmente pela tela"""
        #Atualiza a posição exata do projétil
        self.y -= self.configuracoes.bullet_speed
        #Atualiza a posição do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
            

