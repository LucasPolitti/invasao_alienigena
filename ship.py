import pygame

class Ship:
    """Classe para gerenciar da espaçonave"""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e difine sua posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.configuracoes = ai_game.configuracoes

        #Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        #Coloca cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)

        #Flags de movimento; começa com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da espaçonave com base na flag de movimento"""
        # Atualiza o valor x da espaçonave, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.configuracoes.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.configuracoes.ship_speed

        #Atualiza o objeto rect de self.x
        self.rect.x = self.x

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)