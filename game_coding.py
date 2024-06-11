import tkinter as tk
import coding_text_splitter
import tokenizer


inner_screen_frame_color = '#6C86A6'
font = "Courier New"


class GameCodingScreen:
    outer_frame = None
    screen_switcher = None
    user = None
    regex_pattern = None

    def __init__(self, args):
        self.outer_frame = args[0]
        self.screen_switcher = args[1]
        self.user = args[2]

        self.regex_pattern = coding_text_splitter.create_regex_pattern()
        self.tokenizer = tokenizer.Tokenizer()

        self.screen = tk.Frame(self.outer_frame, background='#D9D9D9')
        self.screen.pack(fill="both", expand=True, padx=25, pady=25)

        coding_top_bar_color = '#F8F8F8'
        self.coding_top_bar = tk.Frame(self.screen, background=coding_top_bar_color, height=100)
        self.coding_top_bar.pack(fill='x')

        self.font_tuple = (font, 30)
        self.coding_label = tk.Label(self.coding_top_bar, text="{task_name}", font=self.font_tuple,
                                     background=coding_top_bar_color)  # replace {task_name} with actual task name later
        self.coding_label.pack(side='left', padx=10)

        self.coding_back_button = tk.Button(self.coding_top_bar, text="X", font=self.font_tuple,
                                            background=coding_top_bar_color,
                                            command=lambda: self.screen_switcher.go_prev_game_screen(self.screen,
                                                                                                     "game_coding"))
        self.coding_back_button.pack(side='right')

        self.coding_task_description_frame = tk.Frame(self.screen, background='#F3F3F3', height=150)
        self.coding_task_description_frame.pack_propagate(False)
        self.coding_task_description_frame.pack(fill='x')

        input_description_frame_color = '#F3F3F3'

        self.input_description_frame = tk.LabelFrame(self.coding_task_description_frame,
                                                     background=input_description_frame_color, width=1200)
        self.input_description_frame.pack_propagate(False)
        self.input_description_frame.pack(side='left', fill='y')

        self.input_first_upper_frame = tk.LabelFrame(self.input_description_frame,
                                                     background=input_description_frame_color, height=50)
        self.input_first_upper_frame.pack_propagate(False)
        self.input_first_upper_frame.pack(fill='x')

        self.font_tuple = (font, 20)
        self.input_label = tk.Label(self.input_first_upper_frame, background=input_description_frame_color,
                                    text="Input:", font=self.font_tuple)
        self.input_label.pack(side='left', padx=5, pady=5)

        self.input_second_upper_frame = tk.Frame(self.input_description_frame, background=input_description_frame_color)
        self.input_second_upper_frame.pack_propagate(False)
        self.input_second_upper_frame.pack(fill='both', expand=True)

        self.input_second_upper_inner_frame = tk.Frame(self.input_second_upper_frame,
                                                       background=input_description_frame_color)
        self.input_second_upper_inner_frame.pack(fill='x')

        self.font_tuple = (font, 10)
        self.input_description = tk.Label(self.input_second_upper_inner_frame, background=input_description_frame_color,
                                          text="2x Integers (separate inputs)", font=self.font_tuple)
        self.input_description.pack(side='left', padx=5, pady=5)

        self.output_description_frame_color = '#DEDEDE'

        self.output_description_frame = tk.LabelFrame(self.coding_task_description_frame,
                                                      background=self.output_description_frame_color)
        self.output_description_frame.pack_propagate(False)
        self.output_description_frame.pack(side='left', fill='both', expand=True)

        self.output_first_upper_frame = tk.LabelFrame(self.output_description_frame,
                                                      background=self.output_description_frame_color, height=50)
        self.output_first_upper_frame.pack_propagate(False)
        self.output_first_upper_frame.pack(fill='x')

        self.font_tuple = (font, 20)
        self.output_label = tk.Label(self.output_first_upper_frame, background=self.output_description_frame_color,
                                     text="Output:", font=self.font_tuple)
        self.output_label.pack(side='left', padx=5, pady=5)

        self.output_second_upper_frame = tk.Frame(self.output_description_frame,
                                                  background=self.output_description_frame_color)
        self.output_second_upper_frame.pack_propagate(False)
        self.output_second_upper_frame.pack(fill='both', expand=True)

        self.output_second_upper_inner_frame = tk.Frame(self.output_second_upper_frame,
                                                        background=self.output_description_frame_color)
        self.output_second_upper_inner_frame.pack(fill='x')

        self.font_tuple = (font, 10)
        self.output_description = tk.Label(self.output_second_upper_inner_frame,
                                           background=self.output_description_frame_color,
                                           text="Sum of Integers that were input.", font=self.font_tuple)
        self.output_description.pack(side='left', padx=5, pady=5)

        self.bottom_frame = tk.Frame(self.screen, background='#6F6F6F')
        self.bottom_frame.pack_propagate(False)
        self.bottom_frame.pack(fill='both', expand=True)

        self.bottom_left_frame = tk.Frame(self.bottom_frame, background='#D9D9D9', width=1200)
        self.bottom_left_frame.pack_propagate(False)
        self.bottom_left_frame.pack(side='left', fill='y')

        self.bottom_left_upper_frame = tk.LabelFrame(self.bottom_left_frame, background='#D9D9D9', height=400)
        self.bottom_left_upper_frame.pack_propagate(False)
        self.bottom_left_upper_frame.pack(fill='x')

        self.font_tuple = (font, 15)
        self.coding_text_entry = tk.Text(self.bottom_left_upper_frame, font=self.font_tuple)
        self.coding_text_entry.pack(fill='both', expand=True, padx=10, pady=10)

        self.bottom_left_lower_frame = tk.LabelFrame(self.bottom_left_frame, background='#DFDFDF')
        self.bottom_left_lower_frame.pack_propagate(False)
        self.bottom_left_lower_frame.pack(fill='both', expand=True)

        self.font_tuple = (font, 40)
        self.run_button = tk.Button(self.bottom_left_lower_frame, text="Run", font=self.font_tuple, width=12, height=2,
                                    command=self.on_run_button_press)
        self.run_button.pack(expand=True)

        self.bottom_right_frame = tk.Frame(self.bottom_frame, background='#6F6F6F')
        self.bottom_right_frame.pack_propagate(False)
        self.bottom_right_frame.pack(side='left', fill='both', expand=True)

        self.output_panel = tk.Text(self.bottom_right_frame, background='#6F6F6F', state='disabled')
        self.output_panel.pack(fill='both', expand=True)

    def on_run_button_press(self):
        text = self.coding_text_entry.get(1.0, tk.END)
        split_text = coding_text_splitter.split_text_elements(text, self.regex_pattern)
        print(split_text)
        tokenized_text = self.tokenizer.tokenize_lines_list(split_text)
        for line in tokenized_text:
            for token in line:
                print([token.token_type, token.token_value])



