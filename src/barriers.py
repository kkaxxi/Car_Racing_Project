import pygame.sprite


class Barrier(pygame.sprite.Sprite):

    def __init__(self, image, position):
        """
        Initializes a new barrier sprite.

        Parameters:
        image (pygame.Surface): The image of the barrier.
        position (tuple): The position of the barrier sprite on the screen.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    def remote(self):
        """
        Removes the barrier sprite if it goes out of bounds.
        """
        if self.rect.top > 800:
            self.kill()

    def update(self):
        """
        Updates the position of the barrier sprite.
        """
        self.rect.y += 3
