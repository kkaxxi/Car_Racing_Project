import pygame
import pygame.freetype
from src.car import MyCar

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('CarRacing')
background_color = (0,0,0)
#background_image = pygame.image.load('game_over.png')
#background_image = pygame.transform.scale(background_image, (500, 800))


def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image


my_car_image = get_car_image('car1.png', size=(100, 70), angle=0)


car = MyCar((250,600), my_car_image)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    car.draw(screen)
    pygame.display.flip()
    clock.tick(60)


#def main():
    ...

#if __name__ == "__main__":
 #   main()