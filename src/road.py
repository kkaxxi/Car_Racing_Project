import pygame.sprite


class Road(pygame.sprite.Sprite):
    def __init__(self, image, position):
        """
        Initialize a new Road object.

        Parameters:
        image (Surface): The image of the road.
        position (tuple): The initial position of the road (x, y).
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    def remove(self):
        """
        Remove the road from the screen when it goes out of view.
        """
        if self.rect.top > 800:
            self.kill()

    def update(self):
        """
        Update the position of the road.
        """
        self.rect.y += 3
