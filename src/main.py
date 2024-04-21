import pygame
import pygame.freetype
from src.car import MyCar
from src.road import Road


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('CarRacing')
background_color = (0,0,0)
#background_image = pygame.image.load('game_over.png')
#background_image = pygame.transform.scale(background_image, (500, 800))


road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)


def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image


my_car_image = get_car_image('imgs/car1.png', size=(100, 90), angle=0)
road_image = pygame.image.load('imgs/road.jpg')
road_image = pygame.transform.scale(road_image, (500, 800))


road = Road(road_image, (250, 400))
road_group.add(road)
road = Road(road_image, (250, 0))
road_group.add(road)


def spawn_road():
    road = Road(road_image, (250,-600))
    road_group.add(road)


def draw_all():
    road_group.update()
    road_group.draw(screen)
    car.draw(screen)




car = MyCar((315,600), my_car_image)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()

    screen.fill(background_color)
    car.move()
    draw_all()
    pygame.display.flip()
    clock.tick(60)


