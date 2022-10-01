from pygame import USEREVENT
from pygame.event import Event

MOVE_UP = Event(USEREVENT + 1)
MOVE_DOWN = Event(USEREVENT + 2)
MOVE_LEFT = Event(USEREVENT + 3)
MOVE_RIGHT = Event(USEREVENT + 4)

AUTO_SAVE = Event(USEREVENT + 7)
