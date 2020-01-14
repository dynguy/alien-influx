import pygame.ftfont

class Button():

    def __init__(self, game_settings, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Creating button dimensions and properties
        self.width = 400
        self.height = 100
        self.button_color = (0, 120, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message preparation
        self.prep_msg(message)

    # Turns the message into a rendered image and center the text on the button
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # Creates the button and draws the message
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
