# -----------------------------------------------------------------------------
# A Clone of Rogue
# Change Log (Who, What, When)
#   KMcGuire, 7/27/25, Created script
#   KMcGuire, 7/28/25, Added @ character, need to fix horizontal movement,
#   created input_handlers.py and actions.py.
#   KMcGuire, 7/30/25, Added entity.py, engine.py. Cleaned main.py.
#   KMcGuire, 8/4/25, Added random map generator
#   KMcGuire, 8/5/25, Added field of view
#------------------------------------------------------------------------------

#!/usr/bin/env python3
import tcod

# Added actions and input handlers

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
#   PyCharm wants to add this height: object
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # Tracking x and y coordinates

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {player, npc}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

# Screen parameters and player position

    with tcod.context.new_terminal(
    screen_width,
    screen_height,
    tileset=tileset,
    title="Rogue Clone",
    vsync=True,
) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()

            engine.handle_event(events)

if __name__ == "__main__":
    main()