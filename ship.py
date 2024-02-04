import pygame

class Ship:
    """Classe para gerenciar da espaçonave"""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e difine sua posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        #Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        #Flags de movimento; começa com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da espaçonave com base na flag de movimento"""
        if self.moving_right:
            self.rect.x += 4
        if self.moving_left:
            self.rect.x -= 4

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)