"""This module holds custom events

We sometimes want multiple different keystrokes to perform the same action,
or for certain events to periodically occur. This module holds the custom event
constants used for that.
"""
from pygame import USEREVENT
from pygame.event import Event

MOVE_UP = Event(USEREVENT + 1)
MOVE_DOWN = Event(USEREVENT + 2)
MOVE_LEFT = Event(USEREVENT + 3)
MOVE_RIGHT = Event(USEREVENT + 4)

AUTO_SAVE = Event(USEREVENT + 7)
