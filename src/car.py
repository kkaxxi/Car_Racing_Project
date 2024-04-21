import pygame.key
import pygame


class MyCar:
    def __init__(self, position, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.game_status = 'game'

    def border(self):
        if self.rect.right > 480:
            self.rect.right = 480
        if self.rect.left < 110:
            self.rect.left = 110

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 4
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 4
        self.border()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def crash(self, sound, barriers):
        for car in barriers:
            if car.rect.colliderect(self.rect):
                print('Game Over')
                #pygame.image.load('imgs/game_over.png').convert_alpha()
                sound.play()
                self.game_status = 'game_over'
