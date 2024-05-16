import pytest
import pygame
from unittest.mock import Mock
from src.button import Button


@pytest.fixture
def button():
    pygame.init()
    return Button(100, 100, 200, 50, "Click me",
                  36, (255, 255, 255), (0, 0, 255), (0, 255, 255), Mock())


def test_button_initialization(button):
    assert button.rect == pygame.Rect(100, 100, 200, 50)
    assert button.text == "Click me"
    assert button.font == 36
    assert button.text_color == (255, 255, 255)
    assert button.button_color == (0, 0, 255)
    assert button.hover_color == (0, 255, 255)
    assert not button.is_hovered


def test_button_draw(button):
    screen = pygame.Surface((300, 200))
    button.draw(screen)


def test_button_handle_event_mousemotion(button):
    event = pygame.event.Event(pygame.MOUSEMOTION, {"pos": (150, 125)})
    button.handle_event(event)
    assert button.is_hovered

    event = pygame.event.Event(pygame.MOUSEMOTION, {"pos": (50, 50)})
    button.handle_event(event)
    assert not button.is_hovered


def test_button_handle_event_mousebuttondown(button):
    button.is_hovered = True
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (150, 125)})
    button.handle_event(event)
    button.action.assert_called_once()

    button.action.reset_mock()
    button.is_hovered = False
    button.handle_event(event)
    button.action.assert_not_called()
