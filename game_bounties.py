import tkinter as tk
from code_inc_widgets import BountyBox

inner_screen_frame_color = '#6C86A6'
font = "Courier New"


class GameBountiesScreen:
    args = None
    outer_frame = None
    screen_switcher = None
    user = None

    def __init__(self, args):
        self.args = args
        self.outer_frame = args[0]
        self.screen_switcher = args[1]
        self.user = args[2]

        self.canvas_color = '#D9D9D9'

        self.screen = tk.Frame(self.outer_frame, background=self.canvas_color)
        self.screen.pack(fill="both", expand=True, padx=25, pady=25)

        bounties_top_bar_color = '#F8F8F8'
        self.bounties_top_bar = tk.Frame(self.screen, background=bounties_top_bar_color, height=100)
        self.bounties_top_bar.pack(fill='x')

        font_tuple = (font, 30)
        self.bounties_label = tk.Label(self.bounties_top_bar, text="Bounties", font=font_tuple,
                                       background=bounties_top_bar_color)
        self.bounties_label.pack(side='left', padx=10)

        self.bounties_back_button = tk.Button(self.bounties_top_bar, text="X", font=font_tuple, background=bounties_top_bar_color,
                                              command=lambda: self.screen_switcher.switch_game_screens(self.screen, 'game_bounties', 'game_home', self.outer_frame, self.screen_switcher, self.user))
        self.bounties_back_button.pack(side='right')

        self.bounties_canvas = tk.Canvas(self.screen, background=self.canvas_color, borderwidth=0)

        self.canvas_scrollbar = tk.Scrollbar(self.screen, command=self.bounties_canvas.yview)
        self.canvas_scrollbar.pack(side="right", fill='y')

        self.bounties_canvas.config(yscrollcommand=self.canvas_scrollbar.set)

        self.bounties_canvas.pack(fill="both", expand=True)

        self.bounties_inner_frame = tk.Frame(self.bounties_canvas, background=self.canvas_color)
        self.canvas_frame = self.bounties_canvas.create_window((0, 0), window=self.bounties_inner_frame, anchor='nw',
                                                               tags="self.bounties_inner_frame")
        self.bounties_inner_frame.bind("<Configure>", self.on_bounties_frame_config)
        self.bounties_canvas.bind("<Configure>", self.on_bounties_canvas_config)

        self.populate_canvas()

    def populate_canvas(self):
        for box_num in range(10):
            BountyBox(self.screen, self.bounties_inner_frame, box_num, self.args)

    def on_bounties_frame_config(self, event):
        # make scroll region encompass inner frame
        self.bounties_canvas.configure(scrollregion=self.bounties_canvas.bbox("all"))

    def on_bounties_canvas_config(self, event):
        # set bounty inner frame width to be equal to canvas width
        canvas_width = event.width
        self.bounties_canvas.itemconfig('self.bounties_inner_frame', width=canvas_width)


