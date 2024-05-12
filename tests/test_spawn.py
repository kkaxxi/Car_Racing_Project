import os
import pytest
import pygame
from src.road import Road
from src.barriers import Barrier
from src.main import spawn_road, spawn_barrier
from unittest.mock import patch

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def screen():
    return pygame.display.set_mode((500, 800))


@pytest.fixture
def road_image():
    return pygame.Surface((500, 800))  # Placeholder image


@pytest.fixture
def barrier_images():
    return [pygame.Surface((30, 50)) for _ in range(2)]  # Placeholder images


@pytest.fixture
def sound_mocker():
    with patch('pygame.mixer.Sound'):
        yield


def test_spawn_road(screen, road_image, sound_mocker):
    road_group = pygame.sprite.Group()
    spawn_road(road_group, road_image)

    assert len(road_group.sprites()) == 1
    road = road_group.sprites()[0]
    assert isinstance(road, Road)


def test_spawn_barrier(screen, barrier_images, sound_mocker):
    barrier_group = pygame.sprite.Group()
    spawn_barrier(barrier_group, barrier_images)

    assert len(barrier_group.sprites()) == 1
    barrier = barrier_group.sprites()[0]
    assert isinstance(barrier, Barrier)
