import tkinter as tk
import screen_switcher

root = tk.Tk()
root.title("Code Inc")
root.geometry("1920x1080")
root.state("zoomed")

test_screen = "home"

if __name__ == '__main__':
    screen_switcher = screen_switcher.ScreenSwitcher(root)
    screen_switcher.switch_screens(None, None, test_screen, screen_switcher, "test_user")


tk.mainloop()
