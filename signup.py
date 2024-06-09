import tkinter as tk
import code_inc_widgets
import json

bg_color = '#AA9595'


class SignupBackButton:
    def __init__(self, screen, screen_switcher):
        self.left_frame = tk.Frame(screen, background=bg_color, width=350)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill='y', expand=False)

        self.font_tuple = ("Courier New", 20)
        self.back_button = tk.Button(self.left_frame, text="Back", width=8, height=2, font=self.font_tuple,
                                     command=lambda: screen_switcher.go_prev_screen(screen, "signup"))
        self.back_button.pack(padx=10, pady=50)


class LoginNavButton:
    def __init__(self, screen, screen_switcher):
        self.right_frame = tk.Frame(screen, background=bg_color, width=350)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill='y', expand=False)

        self.font_tuple = ("Courier New", 20)
        self.login_button = tk.Button(self.right_frame, text="Login", width=8, height=2, font=self.font_tuple,
                                      command=lambda: screen_switcher.switch_screens(screen, "signup", "login_user", screen_switcher))
        self.login_button.pack(side="bottom", padx=10, pady=100)


class SignupScreen:

    screen_switcher = None
    screen = None

    def create_account(self, user_entry, pass_entry, pass_conf_entry):

        username = user_entry.get()
        password = pass_entry.get()
        pass_conf = pass_conf_entry.get()

        if password != pass_conf:
            return
        if username == "" or password == "":
            return

        with open('../data.json', 'r') as openfile:
            current_data = json.load(openfile)

        if username in current_data:
            return

        current_data[user_entry.get()] = pass_entry.get()
        current_data_json = json.dumps(current_data)

        with open('../data.json', 'w') as outfile:
            outfile.write(current_data_json)

        self.screen_switcher.switch_screens(self.screen, "signup", "login_user", self.screen_switcher)

    grey_color = "#D3D3D3"

    def user_entry_focus_in(self, entry):
        if entry.get() == "Username":
            entry.delete(0, tk.END)
            entry.insert(0, '')
            entry.configure(fg="BLACK")

    def user_entry_focus_out(self, entry):
        if entry.get() == '':
            entry.configure(fg=self.grey_color)
            entry.insert(0, "Username")

    def pass_entry_focus_in(self, entry):
        if entry.get() == "Password":
            entry.delete(0, tk.END)
            entry.configure(show="*")
            entry.configure(fg="BLACK")

    def pass_entry_focus_out(self, entry):
        if entry.get() == '':
            entry.configure(show="")
            entry.configure(fg=self.grey_color)
            entry.insert(0, "Password")

    def pass_conf_entry_focus_in(self, entry):
        if entry.get() == "Confirm Password":
            entry.delete(0, tk.END)
            entry.configure(show="*")
            entry.configure(fg="BLACK")

    def pass_conf_entry_focus_out(self, entry):
        if entry.get() == '':
            entry.configure(show="")
            entry.configure(fg=self.grey_color)
            entry.insert(0, "Confirm Password")

    def __init__(self, args):
        self.screen_switcher = args[0]

        font_one = "Courier New"
        self.screen_switcher.root.configure(background=bg_color)

        self.screen = tk.Frame(self.screen_switcher.root, background=bg_color)
        self.screen.pack(fill="both", expand=True)

        self.signup_back_button = SignupBackButton(self.screen, self.screen_switcher)
        self.login_nav_button = LoginNavButton(self.screen, self.screen_switcher)

        center_frame_bg = "#D9D9D9"

        self.center_frame = tk.Frame(self.screen, background="#D9D9D9", width=800, height=1000)
        self.center_frame.pack_propagate(False)
        self.center_frame.pack(fill='y', expand=False)

        self.inner_frame = tk.Frame(self.center_frame, background=center_frame_bg)
        self.inner_frame.pack(expand=True)

        font_tuple = (font_one, 60)
        self.signup_label = tk.Label(self.inner_frame, text="Sign Up", font=font_tuple, background=center_frame_bg)
        self.signup_label.pack()

        entry_width = 20

        font_tuple = (font_one, 40)
        font_color = "#D3D3D3"
        self.user_entry = tk.Entry(self.inner_frame, width=entry_width, font=font_tuple, background="#A4BCCD", fg=font_color)
        self.user_entry.bind("<FocusIn>", lambda event, entry=self.user_entry: self.user_entry_focus_in(entry))
        self.user_entry.bind("<FocusOut>", lambda event, entry=self.user_entry: self.user_entry_focus_out(entry))
        self.user_entry.insert(0, "Username")
        self.user_entry.pack(pady=20)

        entry_pass_bg_color = "#F5F5DF"

        self.pass_entry = tk.Entry(self.inner_frame, width=entry_width, font=font_tuple, background=entry_pass_bg_color, fg=font_color)
        self.pass_entry.bind("<FocusIn>", lambda event, entry=self.pass_entry: self.pass_entry_focus_in(self.pass_entry))
        self.pass_entry.bind("<FocusOut>", lambda event, entry=self.pass_entry: self.pass_entry_focus_out(self.pass_entry))
        self.pass_entry.insert(0, "Password")
        self.pass_entry.pack(pady=20)

        self.pass_conf_entry = tk.Entry(self.inner_frame, width=entry_width, font=font_tuple,
                                        background=entry_pass_bg_color, fg=font_color)
        self.pass_conf_entry.bind("<FocusIn>", lambda event, entry=self.pass_conf_entry: self.pass_conf_entry_focus_in(self.pass_conf_entry))
        self.pass_conf_entry.bind("<FocusOut>", lambda event, entry=self.pass_conf_entry: self.pass_conf_entry_focus_out(self.pass_conf_entry))
        self.pass_conf_entry.insert(0, "Confirm Password")
        self.pass_conf_entry.pack(pady=20)

        font_tuple = (font_one, 50)
        self.create_account_button = tk.Button(self.inner_frame, background=entry_pass_bg_color, text="Create Account", font=font_tuple,
                                               command=lambda: self.create_account(self.user_entry, self.pass_entry, self.pass_conf_entry))
        self.create_account_button.pack(pady=100)
