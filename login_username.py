import tkinter as tk
import code_inc_widgets

bg_color = '#AA9595'


class LoginScreenUsername:
    def __init__(self, args):
        screen_switcher = args[0]

        font_one = "Courier New"
        screen_switcher.root.configure(background=bg_color)

        self.screen = tk.Frame(screen_switcher.root, background=bg_color)
        self.screen.pack(fill="both", expand=True)

        self.left_frame = tk.Frame(self.screen, background=bg_color, width=800)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill='y', expand=False)

        login_illustration = code_inc_widgets.ImgWidget(self.left_frame, "../Images/login_screen_illustration.png", "left", bg_color, (815, 1048), (400, 500))
        font_tuple = (font_one, 40)
        self.sign_up_nav = tk.Button(text="Sign Up", font=font_tuple, command=lambda: screen_switcher.switch_screens(self.screen, "login_user", "signup", screen_switcher))
        self.sign_up_nav_window = login_illustration.image_canvas.create_window(100, 950, anchor='sw', window=self.sign_up_nav)
        login_box = code_inc_widgets.LoginBox(self.screen, screen_switcher, "login_user")
