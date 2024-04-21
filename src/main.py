import random
import pygame
import pygame.freetype
from src.car import MyCar
from src.road import Road
from src.barriers import Barrier

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('CarRacing')
background_color = (0,0,0)
#background_image = pygame.image.load('game_over.png')
#background_image = pygame.transform.scale(background_image, (500, 800))

car_sound = pygame.mixer.Sound('sounds/engine.wav')
car_sound.play(-1)

crash_sound = pygame.mixer.Sound('sounds/crash.wav')

font = pygame.freetype.Font(None, 20)

road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

barrier_group = pygame.sprite.Group()
spawn_barrier_time = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_barrier_time, 1000)


def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image


my_car_image = get_car_image('imgs/car1.png', size=(100, 90), angle=0)
road_image = pygame.image.load('imgs/road.jpg')
road_image = pygame.transform.scale(road_image, (500, 800))

barrier_images = []
barrier1 = get_car_image('imgs/barrier.png', size=(60, 80), angle=0)
barrier2 = get_car_image('imgs/barrier_2.png', size=(60, 80), angle=0)
#barrier3 = get_car_image('imgs/barrier_3.png', size=(70, 90), angle=0)
barrier_images.extend([barrier1, barrier2])

road = Road(road_image, (250, 400))
road_group.add(road)
road = Road(road_image, (250, 0))
road_group.add(road)


def spawn_road():
    road = Road(road_image, (250,-600))
    road_group.add(road)


def spawn_barrier():
    position_y = random.randint(240, 460)  # Випадкова y-координата бар'єру
    lane = random.randint(1, 6)  # Випадково обираємо полосу дороги
    if lane == 1:
        position_x = 165  # Перша полоса
    elif lane == 2:
        position_x = 215  # Друга полоса
    elif lane == 3:
        position_x = 265  # Третя полоса
    elif lane == 4:
        position_x = 315  # Четверта полоса
    elif lane == 5:
        position_x = 365  # П'ята полоса
    else:
        position_x = 415  # Шоста полоса
    barrier = Barrier(random.choice(barrier_images), (position_x, position_y))
    barrier_group.add(barrier)


def draw_all():
    road_group.update()
    road_group.draw(screen)
    barrier_group.update()
    barrier_group.draw(screen)
    car.draw(screen)


car = MyCar((315,600), my_car_image)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()
        if event.type == spawn_barrier_time:
            spawn_barrier()

    screen.fill(background_color)
    if car.game_status == 'game':
        car.move()
        draw_all()
        car.crash(crash_sound, barrier_group)
    if car.game_status == 'game over':
        screen.fill
    pygame.display.flip()
    clock.tick(60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()
        if event.type == spawn_barrier_time:
            spawn_barrier()

    screen.fill(background_color)
    if car.game_status == 'game':
       car.move()
       draw_all()
       car.crash(crash_sound, barrier_group)
    elif car.game_status == 'game_over':
        font.render_to(screen, (30, 300), 'Game Over', (255, 255, 255))
        car_sound.stop()

    pygame.display.flip()
    clock.tick(60)
