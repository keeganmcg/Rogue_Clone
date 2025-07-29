# -----------------------------------------------------------------------------
# A Clone of Rogue
# Change Log (Who, What, When)
#   KMcGuire, 7/27/25, Created script
#   KMcGuire, 7/28/25, Added @ character, need to fix horizontal movement,
#   created input_handlers.py and actions.py.

#------------------------------------------------------------------------------

#!/usr/bin/env python3
import tcod

# Added actions and input handlers

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
#   PyCharm wants to add this height: object
    screen_height = 50

    # Tracking x and y coordinates

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()


# Screen parameters and player position

    with tcod.context.new_terminal(
    screen_width,
    screen_height,
    tileset=tileset,
    title="Rogue Clone",
    vsync=True,
) as context:
        root_console: object = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")
            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()



if __name__ == "__main__":
    main()