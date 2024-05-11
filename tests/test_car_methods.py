import pytest
from unittest.mock import MagicMock
from pygame import Surface
from src.car import MyCar
from unittest.mock import patch
import pygame.key


@pytest.fixture
def car():
    image = Surface((100, 50))  # Mock image
    return MyCar((250, 400), image)


def test_init(car):
    assert car.rect.center == (250, 400)
    assert car.game_status == 'game'


def test_border():
    car = MyCar((0, 0), pygame.Surface((100, 90)))  # Initialize MyCar instance with a surface size similar to the car image
    car.rect.right = 500
    car.rect.left = 100
    car.border()
    assert car.rect.right == 210


def test_move_left(car, mocker):
    mocker.patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: 1})
    initial_x = car.rect.x
    car.move()
    assert car.rect.x == initial_x - 4


def test_draw(car):
    screen = MagicMock()
    car.draw(screen)
    screen.blit.assert_called_once_with(car.image, car.rect)


def test_swap_img(car):
    new_image = Surface((100, 50))  # Mock new image
    car.swap_img(new_image)
    assert car.image == new_image


def test_crash(car):
    sound = MagicMock()
    barrier = MagicMock()
    barrier.rect.colliderect.return_value = True
    barriers = [barrier]
    car.crash(sound, barriers)
    assert sound.play.called
    assert car.game_status == 'game_over'
