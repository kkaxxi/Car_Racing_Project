import pygame
import pytest
from src.road import Road


@pytest.fixture
def road():
    image = pygame.Surface((100, 100))  # Создаем заглушечное изображение
    return Road(image, (250, 0))  # Создаем экземпляр класса Road для тестов


def test_initial_position(road):
    assert road.rect.center == (250, 0)  # Проверяем начальное положение дороги


def test_remove(road):
    road.rect.top = 801  # Помещаем дорогу за пределы экрана
    road.remove()  # Вызываем метод удаления
    assert not road.alive()  # Проверяем, что дорога была удалена


def test_update(road):
    initial_y = road.rect.y  # Запоминаем начальное положение по оси y
    road.update()  # Вызываем метод обновления
    assert road.rect.y == initial_y + 3
