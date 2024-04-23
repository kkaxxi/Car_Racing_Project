import random
import pygame
import pygame.freetype
from src.car import MyCar
from src.road import Road
from src.barriers import Barrier
import os
from button import Button

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('CarRacing')
background_color = (0,0,0)

#project_root = os.getenv('PROJECT_ROOT', '.')

car_sound_path = os.path.join('sounds', 'engine.wav')
crash_sound_path = os.path.join('sounds', 'crash.wav')


car_sound = pygame.mixer.Sound(car_sound_path)
car_sound.play(-1)
crash_sound = pygame.mixer.Sound(crash_sound_path)

#car_sound = pygame.mixer.Sound('../sounds/engine.wav')

#crash_sound = pygame.mixer.Sound('../sounds/crash.wav')

#font = pygame.freetype.Font(None, 20)

road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

barrier_group = pygame.sprite.Group()
spawn_barrier_time = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_barrier_time, 1000)


def get_car_image(filename, size, angle):
    """
    Load and transform the car image.

    This function loads an image file, resizes it, and rotates it according to the specified angle.

    Parameters:
    filename (str): The filename of the image to load.
    size (tuple): A tuple containing the width and height to resize the image to.
    angle (int): The angle in degrees to rotate the image by.

    Returns:
    pygame.Surface: The transformed car image.
    """
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image

"""
my_car_image = get_car_image('../imgs/car1.png', size=(100, 90), angle=0)
road_image = pygame.image.load('../imgs/road.jpg')
road_image = pygame.transform.scale(road_image, (500, 800))

barrier_images = []
barrier1 = get_car_image('../imgs/barrier.png', size=(60, 80), angle=0)
barrier2 = get_car_image('../imgs/barrier_2.png', size=(60, 80), angle=0)
#barrier3 = get_car_image('imgs/barrier_3.png', size=(70, 90), angle=0)
barrier_images.extend([barrier1, barrier2])

game_over_image = pygame.image.load('../imgs/game_over.png')
game_over_image = pygame.transform.scale(game_over_image, (500, 500))
x = (screen.get_width() - game_over_image.get_width()) // 2
y = (screen.get_height() - game_over_image.get_height()) // 2
"""
my_car_image_path = os.path.join('imgs', 'car1.png')
road_image_path = os.path.join('imgs', 'road.jpg')
barrier1_image_path = os.path.join('imgs', 'barrier.png')
barrier2_image_path = os.path.join('imgs', 'barrier_2.png')
game_over_image_path = os.path.join('imgs', 'game_over.png')
select_car_image_path = os.path.join('imgs', 'select_car.png')

my_car_image = get_car_image(my_car_image_path, size=(100, 90), angle=0)
road_image = pygame.image.load(road_image_path)
road_image = pygame.transform.scale(road_image, (500, 800))
select_car_image = get_car_image(select_car_image_path, size=(500, 500), angle=0)

barrier_images = []
barrier1 = get_car_image(barrier1_image_path, size=(60, 80), angle=0)
barrier2 = get_car_image(barrier2_image_path, size=(60, 80), angle=0)
barrier_images.extend([barrier1, barrier2])

game_over_image = pygame.image.load(game_over_image_path)
game_over_image = pygame.transform.scale(game_over_image, (500, 500))
x = (screen.get_width() - game_over_image.get_width()) // 2
y = (screen.get_height() - game_over_image.get_height()) // 2


road = Road(road_image, (250, 400))
road_group.add(road)
road = Road(road_image, (250, 0))
road_group.add(road)


def spawn_road():
    """
    Spawn a new road object.

    This function creates a new instance of the Road class and adds it to the road_group sprite group.
    """
    road = Road(road_image, (250,-600))
    road_group.add(road)


def spawn_barrier():
    """
    Spawn a new barrier object.

    This function generates random coordinates for the barrier's position and selects a random image from barrier_images.
    The barrier is then created using the selected image and position, and added to the barrier_group sprite group.
    """
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
    """
    Draw all game objects on the screen.

    This function updates and draws all objects in the road_group and barrier_group sprite groups,
    as well as the car object.
    """
    road_group.update()
    road_group.draw(screen)
    barrier_group.update()
    barrier_group.draw(screen)
    car.draw(screen)

#select car
pause = False

def buttony_action():
    car_image = get_car_image('imgs/car1.png', size=(100, 90), angle=0)
    car.swap_img(car_image)

def buttonr_action():

    car_image = get_car_image('imgs/car3.png', size=(100, 90), angle=0)
    car.swap_img(car_image)

def buttonw_action():
    car_image = get_car_image('imgs/car2.png', size=(100, 90), angle=0)
    car.swap_img(car_image)

def button_start_action():
    barrier_group.empty()
    car.game_status = 'game'

def pause_button_action():
    global pause
    pause = True

buttony = Button(210,150,80,20,"Select", 36, (255,255,255), (0,0,255), (0,255, 255), buttony_action)
buttonr = Button(210,310,80,20,"Select", 36, (255,255,255), (0,0,255), (0,255, 255), buttonr_action)
buttonw = Button(210,495,80,20,"Select", 36, (255,255,255), (0,0,255), (0,255, 255), buttonw_action)
button_start = Button(210,700,80,20,"Start", 36, (255,255,255), (0,0,255), (0,255, 255), button_start_action)
pause_button = Button(410,10,80,20,"Pause", 36, (255,255,255), (0,0,255), (0,255, 255), pause_button_action)



car = MyCar((315,600), my_car_image)

car.game_status = 'pre game'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()
        if event.type == spawn_barrier_time:
            spawn_barrier()
        buttony.handle_event(event)
        buttonr.handle_event(event)
        buttonw.handle_event(event)
        button_start.handle_event(event)
        pause_button.handle_event(event)

    screen.fill(background_color)

    if car.game_status == 'pre game':
        screen.blit(select_car_image,(0,0))

        buttony.draw(screen)
        buttonr.draw(screen)
        buttonw.draw(screen)
        button_start.draw(screen)

        pygame.mixer.pause()

    if car.game_status == 'game':
        car.move()
        draw_all()
        car.crash(crash_sound, barrier_group)

        pause_button.draw(screen)

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
        screen.blit(game_over_image,(x, y))
        pygame.display.flip()
        #font.render_to(screen, (30, 300), 'Game Over', (255, 255, 255))
        car_sound.stop()

    pygame.display.flip()
    clock.tick(60)
