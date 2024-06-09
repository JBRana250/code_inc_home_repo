import tkinter as tk

bg_color = '#AA9595'
outer_screen_frame_color = '#D9D9D9'
inner_screen_frame_color = '#6C86A6'

font = "Courier New"


class HomeScreen:
    def __init__(self, args):
        screen_switcher = args[0]
        user = args[1]

        self.screen = tk.Frame(screen_switcher.root, background=bg_color)
        self.screen.pack(fill="both", expand=True)

        self.outer_screen_frame = tk.Frame(self.screen, background=outer_screen_frame_color)
        self.outer_screen_frame.pack(fill="both", expand=True)

        self.inner_screen_frame = tk.Frame(self.outer_screen_frame, background=inner_screen_frame_color)
        self.inner_screen_frame.pack(fill="both", expand=True, padx=50, pady=50)

        self.inner_top_frame = tk.Frame(self.inner_screen_frame, background=inner_screen_frame_color, height=100)
        self.inner_top_frame.pack_propagate(False)
        self.inner_top_frame.pack(fill="x", expand=False)

        self.inner_mid_frame = tk.Frame(self.inner_screen_frame, background=inner_screen_frame_color, height=400)
        self.inner_mid_frame.pack_propagate(False)
        self.inner_mid_frame.pack(fill="x", expand=False)

        self.inner_bot_frame = tk.Frame(self.inner_screen_frame, background=inner_screen_frame_color, height=1000)
        self.inner_bot_frame.pack_propagate(False)
        self.inner_bot_frame.pack(fill="both", expand=False)

        self.font_tuple = (font, 20)
        self.back_button = tk.Button(self.inner_top_frame, text="Back", width=8, height=2, font=self.font_tuple,
                                     command=lambda: screen_switcher.go_prev_screen(self.screen, "home"))
        self.back_button.pack(padx=10, pady=10, side="left")

        self.font_tuple = (font, 200)
        self.title_label = tk.Label(self.inner_mid_frame, text="Code Inc.", font=self.font_tuple,
                                    background=inner_screen_frame_color)
        self.title_label.pack(pady=50)

        self.bot_mid_frame = tk.Frame(self.inner_bot_frame, background=inner_screen_frame_color)
        self.bot_mid_frame.pack(expand=True)

        self.font_tuple = (font, 50)
        self.settings_button = tk.Button(self.bot_mid_frame, text="Settings", width=8, height=2, font=self.font_tuple,
                                         command=lambda: screen_switcher.switch_screens(self.screen, "home", "settings",
                                                                                        screen_switcher, user))
        self.settings_button.pack(padx=10, pady=10, side="left")

        self.play_button = tk.Button(self.bot_mid_frame, text="Play", width=8, height=2, font=self.font_tuple,
                                     command=lambda: screen_switcher.switch_screens(self.screen, "home", "game",
                                                                                    screen_switcher, user))
        self.play_button.pack(padx=100, pady=10, side="left")

        self.help_button = tk.Button(self.bot_mid_frame, text="Help", width=8, height=2, font=self.font_tuple,
                                     command=lambda: screen_switcher.switch_screens(self.screen, "home", "help",
                                                                                    screen_switcher, user))
        self.help_button.pack(padx=10, pady=10, side="left")
