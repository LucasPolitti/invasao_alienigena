import pygame

class Ship:
    """Calsse para cuidar da espaçonave"""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e difine sua posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        #Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)