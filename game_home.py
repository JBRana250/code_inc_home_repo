import tkinter as tk

inner_screen_frame_color = '#6C86A6'
font = "Courier New"


class GameHomeScreen:
    def __init__(self, args):
        outer_frame = args[0]
        screen_switcher = args[1]
        user = args[2]

        self.screen = tk.Frame(outer_frame, background=inner_screen_frame_color)
        self.screen.pack(fill="both", expand=True, padx=25, pady=25)

        self.inner_frame = tk.Frame(self.screen, background=inner_screen_frame_color)
        self.inner_frame.pack(fill="both", expand=True, padx=25, pady=25)

        self.upper_inner_frame = tk.Frame(self.inner_frame, background=inner_screen_frame_color)
        self.upper_inner_frame.pack(side="top", fill='x')

        self.font_tuple = (font, 25)
        self.bounty_nav = tk.Button(self.upper_inner_frame, background="RED", text="Bounties", font=self.font_tuple, width=8, height=4,
                                    command=lambda: screen_switcher.switch_game_screens(self.screen, "game_home", "game_bounties", outer_frame, screen_switcher, user))
        self.bounty_nav.pack(side="left")

        self.font_tuple = (font, 15)
        self.docs_nav = tk.Button(self.upper_inner_frame, background="GREEN", text="Python Docs", font=self.font_tuple, width=14, height=7)
        self.docs_nav.pack(side="left", padx=50)
