import tkinter as tk
import code_inc_widgets
import game_home
import game_bounties

bg_color = '#AA9595'

outer_screen_frame_color = '#C3C3C3'
inner_screen_frame_color = '#6C86A6'

font = "Courier New"


class GameScreen:
    def __init__(self, args):
        screen_switcher = args[0]
        user = args[1]

        self.screen = tk.Frame(screen_switcher.root, background=bg_color)
        self.screen.pack(fill="both", expand=True)

        self.top_bar = code_inc_widgets.TopBar(self.screen)

        self.outer_screen_frame = tk.Frame(self.screen, background=outer_screen_frame_color)
        self.outer_screen_frame.pack(fill="both", expand=True)

        screen_switcher.switch_game_screens(None, None, "game_home", self.outer_screen_frame, screen_switcher, user)
