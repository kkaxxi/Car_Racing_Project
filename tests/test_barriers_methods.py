import pygame
import pytest
from src.barriers import Barrier


@pytest.fixture
def barrier():
    image = pygame.Surface((100, 100))  # Создаем заглушечное изображение
    return Barrier(image, (250, 0))  # Создаем экземпляр класса Road для тестов


def test_initial_position(barrier):
    assert barrier.rect.center == (250, 0)  # Проверяем начальное положение


def test_remove(barrier):
    barrier.rect.top = 801  # Помещаем дорогу за пределы экрана
    barrier.remove()  # Вызываем метод удаления
    assert not barrier.alive()  # Проверяем, что дорога была удалена


def test_update(barrier):
    initial_y = barrier.rect.y  # Запоминаем начальное положение по оси y
    barrier.update()  # Вызываем метод обновления
    assert barrier.rect.y == initial_y + 3
