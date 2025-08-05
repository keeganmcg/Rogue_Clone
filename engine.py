# -----------------------------------------------------------------------------
# A Clone of Rogue
# Change Log (Who, What, When)
# KMcGuire, Created script, 7/30/25
#------------------------------------------------------------------------------

# Importing controllers from other files

from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

import game_map

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# Defining what the Engine can do

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_event(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()
