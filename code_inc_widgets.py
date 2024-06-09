import tkinter as tk
from PIL import ImageTk, Image
import json

bg_color = '#AA9595'
login_box_bg_color = '#949494'
font_family = "Courier New"


def login_with_user(username, screen_switcher, current_screen, current_screen_text):
    if username == "":
        return
    with open('../data.json', 'r') as openfile:
        current_data = json.load(openfile)
    if username not in current_data:
        return
    screen_switcher.switch_screens(current_screen, current_screen_text, "login_pass", screen_switcher, username)


def login_with_pass(user, password, screen_switcher, current_screen, current_screen_text):
    if password == "":
        return
    with open('../data.json', 'r') as openfile:
        current_data = json.load(openfile)
    if password != current_data[user]:
        return
    screen_switcher.switch_screens(current_screen, current_screen_text, "home", screen_switcher, user)


class LoginBox:
    def __init__(self, *args):
        parent = args[0]
        screen_switcher = args[1]
        current_screen_text = args[2]
        user = None
        if len(args) > 3:
            user = args[3]

        self.box_frame = tk.Frame(parent, background=bg_color, width=1300)
        self.box_frame.pack_propagate(False)
        self.box_frame.pack(side="right", fill='y', expand=False)

        self.box = tk.Frame(self.box_frame, background=login_box_bg_color, height=400, width=800)
        self.box.pack_propagate(False)
        self.box.pack(fill='none', expand=True)

        self.inner_frame = tk.Frame(self.box, background=login_box_bg_color)
        self.inner_frame.pack(expand=True)

        font_tuple = (font_family, 70)
        text = ""
        if current_screen_text == "login_user":
            text = "Username"
        elif current_screen_text == "login_pass":
            text = "Password"
        else:
            print("error with current_screen_text")
        self.label = tk.Label(self.inner_frame, background=login_box_bg_color, text=text, font=font_tuple)
        self.label.pack(pady=20)

        font_tuple = (font_family, 20)
        self.entry = tk.Entry(self.inner_frame, width=30, font=font_tuple)
        self.entry.pack()

        if current_screen_text == "login_user":
            font_tuple = (font_family, 20)
            self.continue_button = tk.Button(self.inner_frame, text="Next", width=8, height=2, font=font_tuple,
                                             command=lambda: login_with_user(self.entry.get(), screen_switcher, parent, current_screen_text))
            self.continue_button.pack(pady=20)

        if current_screen_text == "login_pass":
            self.entry.configure(show="*")
            self.button_frame = tk.Frame(self.inner_frame, background=login_box_bg_color)
            self.button_frame.pack(expand=True, pady=20)

            self.back_button = tk.Button(self.button_frame, text="Back", width=8, height=2, font=font_tuple,
                                         command=lambda: screen_switcher.switch_screens(parent, current_screen_text, "login_user", screen_switcher))
            self.back_button.pack(side="left", padx=10)

            self.continue_button = tk.Button(self.button_frame, text="Next", width=8, height=2, font=font_tuple,
                                             command=lambda: login_with_pass(user, self.entry.get(), screen_switcher, parent, current_screen_text))
            self.continue_button.pack(side="left", padx=10)


class TopBar:
    def __init__(self, screen):
        font = "Courier New"
        top_bar_color = '#D9D9D9'
        self.top_bar = tk.Frame(screen, background=top_bar_color, height=125)
        self.top_bar.pack_propagate(False)
        self.top_bar.pack(fill='x')

        self.top_bar_left_frame = tk.Frame(self.top_bar, background=top_bar_color)
        self.top_bar_left_frame.pack(side="left", padx=10)

        self.font_tuple = (font, 20)
        self.pause_button = tk.Button(self.top_bar_left_frame, background='#C1C1C1', text="Pause", width=8, height=3,
                                      font=self.font_tuple)
        self.pause_button.pack(side="left", padx=10)

        self.font_tuple = (font, 50)
        self.day_label = tk.Label(self.top_bar_left_frame, text="Day 1", background=top_bar_color, font=self.font_tuple)
        self.day_label.pack(side="left", padx=20)

        self.top_bar_mid_frame = tk.Frame(self.top_bar, background='#ADADAD', width=300, height=100)
        self.top_bar_mid_frame.pack_propagate(False)
        self.top_bar_mid_frame.pack(side="left", padx=400)

        self.top_bar_mid_inner_frame = tk.Frame(self.top_bar_mid_frame, background='#E3AAAA', width=275, height=80)
        self.top_bar_mid_inner_frame.pack_propagate(False)
        self.top_bar_mid_inner_frame.pack(padx=10, pady=10)

        self.font_tuple = (font, 30)
        self.income_quota_label = tk.Label(self.top_bar_mid_inner_frame, text="25g / 50g", background='#E3AAAA',
                                           font=self.font_tuple)
        self.income_quota_label.pack(pady=20)

        self.top_bar_right_frame = tk.Frame(self.top_bar, background=top_bar_color)
        self.top_bar_right_frame.pack(side="left")

        self.time_label = tk.Label(self.top_bar_right_frame, text="Time Left: 234s", font=self.font_tuple,
                                   background=top_bar_color)
        self.time_label.pack()

class BountyBox:
    def __init__(self, screen, bounties_inner_frame, box_num, args):
        self.screen_switcher = args[1]
        font = "Courier New"
        bounty_box_color = '#F4F4F4'
        box = tk.Frame(bounties_inner_frame, background=bounty_box_color, height=250, width=1)
        box.pack_propagate(False)
        box.pack(fill='x', expand=True, padx=25, pady=25)

        left_frame = tk.LabelFrame(box, background=bounty_box_color, width=700)
        left_frame.pack_propagate(False)
        left_frame.pack(side="left", fill='y')

        left_upper_frame = tk.LabelFrame(left_frame, background=bounty_box_color, height=100)
        left_upper_frame.pack_propagate(False)
        left_upper_frame.pack(fill='x')

        delete_bounty_button = tk.Button(left_upper_frame, text="X", height=3, width=7, background="#DC6060",
                                            command=lambda: self.delete_bounty(box)) # make functionality later after randomisation and creation of bounty system
        delete_bounty_button.pack(side="left", padx=10)

        font_tuple = (font, 30)
        bounty_label = tk.Label(left_upper_frame, text="test_bounty " + str(box_num+1), font=font_tuple, background=bounty_box_color)
        bounty_label.pack(side="left")

        difficulty_label_frame = tk.Frame(left_frame, background=bounty_box_color)
        difficulty_label_frame.pack(fill='x')

        difficulty_label = tk.Label(difficulty_label_frame, text="Difficulty: test", font=font_tuple, background=bounty_box_color)
        difficulty_label.pack(side='left', padx=10, pady=10)

        mid_frame_color = '#EFEFEF'
        mid_frame = tk.LabelFrame(box, background=mid_frame_color, width=600)
        mid_frame.pack_propagate(False)
        mid_frame.pack(side="left", fill='y')

        mid_upper_frame = tk.Frame(mid_frame, background=mid_frame_color)
        mid_upper_frame.pack(side='top', fill='x')

        task_description = tk.Label(mid_upper_frame, text="task_description", font=font_tuple, background=mid_frame_color)
        task_description.pack(side='left', padx=10, pady=10)

        right_frame = tk.LabelFrame(box, background=bounty_box_color)
        right_frame.pack_propagate(False)
        right_frame.pack(side='left', fill='both', expand=True)

        right_upper_frame = tk.LabelFrame(right_frame, background=bounty_box_color, height=100)
        right_upper_frame.pack_propagate(False)
        right_upper_frame.pack(fill='x')

        font_tuple = (font, 20)
        time_label = tk.Label(right_upper_frame, background=bounty_box_color, text="Time: 60s", font=font_tuple)
        time_label.pack(side="left", padx=10, pady=10)

        money_label = tk.Label(right_upper_frame, background=bounty_box_color, text="Money: 10g", font=font_tuple)
        money_label.pack(side="left", padx=50)

        take_bounty_frame = tk.Frame(right_frame, background=bounty_box_color)
        take_bounty_frame.pack(fill='x')

        take_bounty_button = tk.Button(take_bounty_frame, background='#D9D9D9', text="Take", font=font_tuple, height=4, width=12,
                                        command=lambda: self.screen_switcher.switch_game_screens(screen, "game_bounties", "game_coding", args[0], args[1], args[2])) # implement different bounty data into this later
        take_bounty_button.pack(pady=20)

    def delete_bounty(self, box):
        print("delete")

class ImgWidget:
    def __init__(self, parent, img_file, pack_side, bg_color, img_size, img_location_args):
        global img  # need to make it a global variable or else it will be garbage collected
        img = ImageTk.PhotoImage(Image.open(img_file).resize(size=img_size))
        self.image_canvas = tk.Canvas(parent, background=bg_color, width=img_size[0], height=img_size[1],
                                      highlightthickness=0)
        self.image_canvas.pack(side=pack_side)

        self.image_canvas.create_image(img_location_args[0], img_location_args[1], image=img)