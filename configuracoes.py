class Configuracoes:
    """Classe para armazenar as configurações do Jogo Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        #Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 100, 230)
        self.ship_speed = 4
        #Configurações de projétil
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = (60, 60, 60)
