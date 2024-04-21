import pygame.key
import pygame


class MyCar:
    def __init__(self, position, image):
        """
        Initializes a new instance of the MyCar class.

        Parameters:
        position (tuple): The initial position of the car.
        image (pygame.Surface): The image representing the car.
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.game_status = 'game'

    def border(self):
        """
        Ensures the car stays within the boundaries of the game window.
        """
        if self.rect.right > 480:
            self.rect.right = 480
        if self.rect.left < 110:
            self.rect.left = 110

    def move(self):
        """
        Moves the car left or right based on user input.
        """
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= 4
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += 4
        self.border()

    def draw(self, screen):
        """
        Draws the car on the screen.

        Parameters:
        screen (pygame.Surface): The surface on which the car will be drawn.
        """
        screen.blit(self.image, self.rect)

    def crash(self, sound, barriers):
        """
        Checks for collisions with barriers and changes game status if necessary.

        Parameters:
        sound (pygame.mixer.Sound): The sound to play in case of a crash.
        barriers (pygame.sprite.Group): The group of barrier objects to check for collisions.
        """
        for car in barriers:
            if car.rect.colliderect(self.rect):
                print('Game Over')
                sound.play()
                self.game_status = 'game_over'
