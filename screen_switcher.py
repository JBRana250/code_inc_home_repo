import tkinter as tk

import login_username
import login_password
import signup
import home
import game
import game_home
import game_bounties
import game_coding


class ScreenSwitcher:
    root = None
    prev_screen = None
    current_screen = None

    prev_game_screen = None
    current_game_screen = None

    current_screen_args = ()  # to supplement prev_screen_args
    prev_screen_args = ()  # contains arguments of previous screen

    current_game_screen_args = ()
    prev_game_screen_args = ()

    text_to_screen_map = {
        "login_user": login_username.LoginScreenUsername,
        "login_pass": login_password.LoginScreenPassword,
        "signup": signup.SignupScreen,
        "home": home.HomeScreen,
        "game": game.GameScreen
    }

    text_to_game_screen_map = {
        "game_home": game_home.GameHomeScreen,
        "game_bounties": game_bounties.GameBountiesScreen,
        "game_coding": game_coding.GameCodingScreen
    }

    def switch_screens(self, current_screen, current_screen_text, next_screen,
                       *args):  # params is list with needed parameters
        if current_screen is not None:
            current_screen.destroy()
        if next_screen is not None:
            self.prev_screen = current_screen_text
            self.current_screen = next_screen
            self.prev_screen_args = self.current_screen_args  # set prev screen args first
            self.current_screen_args = args  # THEN set current screen args

            self.text_to_screen_map[next_screen](self.current_screen_args)

    def switch_game_screens(self, current_screen, current_screen_text, next_screen,
                            *args):  # this is for switching inner screen INSIDE game screen
        if current_screen is not None:

            current_screen.destroy()
        if next_screen is not None:
            self.prev_game_screen = current_screen_text
            self.current_game_screen = next_screen
            self.prev_game_screen_args = self.current_game_screen_args  # set prev screen args first
            self.current_game_screen_args = args  # THEN set current screen args

            self.text_to_game_screen_map[next_screen](self.current_game_screen_args)

    def go_prev_screen(self, current_screen, current_screen_text):
        if current_screen is not None:
            current_screen.destroy()

        self.current_screen = self.prev_screen  # sets the value of current_screen to current value of prev_screen

        self.text_to_screen_map[self.prev_screen](self.prev_screen_args)  # go to the prev screen

        self.prev_screen = current_screen_text  # THEN sets new value for prev_screen

    def go_prev_game_screen(self, current_screen, current_screen_text):
        if current_screen is not None:
            current_screen.destroy()

        self.current_game_screen = self.prev_game_screen  # sets the value of current_screen to current value of prev_screen

        self.text_to_game_screen_map[self.prev_game_screen](self.prev_game_screen_args)  # go to the prev screen

        self.prev_game_screen = current_screen_text  # THEN sets new value for prev_screen

    def __init__(self, root):
        self.root = root
