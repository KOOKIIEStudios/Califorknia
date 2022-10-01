"""This module handles input-listening

This allows conversion of PyGame key-related events to be converted into
a form that the World object can pass on to its entities.
"""
import pygame

from constants import events


CONTROL_KEYS = (pygame.K_LCTRL, pygame.K_RCTRL)


def listen_input() -> None:
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
        pygame.event.post(events.MOVE_UP)
    if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
        pygame.event.post(events.MOVE_DOWN)
    if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
        pygame.event.post(events.MOVE_LEFT)
    if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
        pygame.event.post(events.MOVE_RIGHT)


def is_pause_toggled(event: pygame.event) -> bool:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return True
    return False


def is_menu_toggled(event: pygame.event) -> bool:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_TAB:
            return True
    return False


def is_start_running(event: pygame.event) -> bool:
    if event.type == pygame.KEYDOWN:
        if event.key in CONTROL_KEYS:
            return True
    return False


def is_stop_running(event: pygame.event) -> bool:
    if event.type == pygame.KEYUP:
        if event.key in CONTROL_KEYS:
            return True
    return False
