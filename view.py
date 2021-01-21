from tkinter import *
from resources import *


class View(Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title(TITLE)
        self.iconphoto(False, PhotoImage(file='images/icon.png'))
        self.geometry(RESOLUTION)
        self.resizable(0, 0)
        self.score = StringVar(self)
        self.label_word = StringVar(self)
        self.configure(bg=BG_COLOR)
        self.images = IMAGES
        self.title_label = Label(self, text=TITLE, background=BG_COLOR, font=LARGE_FONT)
        self.choose_label = Label(self, text='wybierz kategorię', background=BG_COLOR, font=MED_FONT)
        self.category = StringVar(self)
        self.category.set(CATEGORIES[0])
        self.category.trace("w", self.change_category)

        self.option_menu = OptionMenu(self, self.category, *CATEGORIES)
        self.option_menu.configure(background=BTN_COLOR, font=MED_FONT, borderwidth='1',
                                   highlightthickness='0', activebackground=BTN_ACT_COLOR, width=15)
        menu = self.nametowidget(self.option_menu.menuname)
        menu.config(font=MED_FONT, background=BG_COLOR, activebackground=BTN_COLOR)
        self.start_button = Button(self, text='start', width=15, height=1,
                                   command=lambda: self.controller.new_game(), background=BTN_COLOR,
                                   font=MED_FONT, activebackground=BTN_ACT_COLOR, relief=GROOVE)
        self.exit_button = Button(self, text='wyjście', width=15, height=1, command=lambda: self.quit_game(),
                                  background=BTN_COLOR, font=MED_FONT, activebackground=BTN_ACT_COLOR, relief=GROOVE)

        self.hangman_label = Label(self)
        self.word_label = Label(self, textvariable=self.label_word, font=WORD_LBL_FONT,
                                background=BG_COLOR)
        self.category_label = Label(self, textvariable=self.category, font=MED_FONT,
                                    background=BG_COLOR)
        self.new_game_btn = Button(self, text='nowa gra', width=15, height=1,
                                   command=lambda: self.controller.build_menu(), background=BTN_COLOR, font=MED_FONT,
                                   activebackground=BTN_ACT_COLOR, relief=GROOVE)
        self.points_label = Label(self, text='punkty', background=BG_COLOR, font=SMALL_FONT)
        self.points_counter = Label(self, textvariable=self.score, background=BG_COLOR,
                                    font=MED_FONT)

        for i, img in enumerate(IMAGES):
            self.images[i] = PhotoImage(file=img).subsample(2, 2)

    def main(self):
        self.mainloop()

    def build_menu(self):
        self.clear_grid()
        self.title_label.place(relx=.5, rely=.2, anchor="c")
        self.choose_label.place(relx=.5, rely=.4, anchor="c")
        self.option_menu.place(relx=.5, rely=.5, anchor="c")
        self.start_button.place(relx=.5, rely=.6, anchor="c")
        self.exit_button.place(relx=.5, rely=.72, anchor="c", )

    def build_interface(self):
        self.clear_place()
        self.score.set('0')
        self.label_word.set(' '.join('_' * len(self.controller.model.word)))
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        for num, letter in enumerate(LETTERS):
            Button(self, text=letter, width=7, height=1, background=KEY_BG_COLOR, activebackground=KEY_BG_ACT_COLOR,
                   command=lambda row=num: self.controller.model.guess_letter(LETTERS[row]), relief=GROOVE,
                   font=WORD_LBL_FONT).grid(row=6 + num // 11, column=num % 11, sticky=N + S + E + W)
        self.hangman_label.grid(row=0, column=0, columnspan=5, rowspan=5, sticky=N + W, padx=5, pady=5)
        self.hangman_label.config(image=self.images[0], border=10, background=BTN_ACT_COLOR)
        self.title_label.grid(row=0, column=5, columnspan=5)
        self.word_label.grid(row=4, column=0, columnspan=5, sticky=W)
        self.category_label.grid(row=1, column=5, columnspan=5, padx=5, pady=5)
        self.new_game_btn.grid(row=2, column=5, columnspan=5, padx=5, pady=5)
        self.exit_button.grid(row=3, column=5, columnspan=5, padx=5, pady=5)
        self.points_counter.grid(row=4, column=5, columnspan=5, sticky=S)
        self.points_label.grid(row=5, column=5, columnspan=5, sticky=N)

    def clear_place(self):
        self.title_label.place_forget()
        self.choose_label.place_forget()
        self.option_menu.place_forget()
        self.start_button.place_forget()
        self.exit_button.place_forget()
        items = self.place_slaves()
        for item in items:
            item.destroy()

    def clear_grid(self):
        self.hangman_label.grid_forget()
        self.title_label.grid_forget()
        self.word_label.grid_forget()
        self.category_label.grid_forget()
        self.new_game_btn.grid_forget()
        self.exit_button.grid_forget()
        self.points_label.grid_forget()
        self.points_counter.grid_forget()
        items = self.grid_slaves()
        for item in items:
            item.destroy()

    def change_category(self, *params):
        return self.category.get()

    def quit_game(self):
        self.destroy()
