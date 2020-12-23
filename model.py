from tkinter.messagebox import showinfo
import random

from words_database import *


class Model:
    CHANCES = 10

    def __init__(self, controller):
        self.controller = controller
        self.category = None
        self.score_points = 0
        self.number_of_guesses = 0
        self.word = None
        self.guess = None
        self.used_words = list()

    def new_game(self):
        self.score_points = 0
        self.number_of_guesses = 0
        self.category = self.controller.change_category()
        self.word = self.get_word()
        print(self.word)
        self.used_words.append(self.word)
        self.guess = ' '.join(self.word)

    def get_word(self):
        word = random.choice(eval(self.category))
        return word.upper()

    def guess_letter(self, letter):
        if self.number_of_guesses < self.CHANCES:
            text = list(self.guess)
            guessed = list(self.controller.view.label_word.get())
            if self.guess.count(letter) > 0:
                for c in range(len(text)):
                    if text[c] == letter:
                        guessed[c] = letter
                    self.controller.view.label_word.set(''.join(guessed))
                    if self.controller.view.label_word.get() == self.guess:
                        showinfo("Zwycięstwo!", "Twój dotychczasowy wynik to: " + str(self.score_points + 1))

                        self.word = self.get_word()
                        while self.word in self.used_words:
                            if len(self.used_words) == len(self.category):
                                showinfo("Zwycięstwo!",
                                         "Udało ci się odgadnąć wszystkie słowa w tej kategorii, twój ostateczny "
                                         "wynik to: " + str(
                                             self.score_points + 1))
                                self.new_game()
                                break
                            self.word = self.get_word()
                        self.score_points += 1
                        self.controller.view.score.set(self.score_points)
                        self.number_of_guesses = 0
                        self.guess = None
                        self.used_words.append(self.word)
                        self.guess = ' '.join(self.word)
                        self.controller.view.label_word.set(' '.join('_' * len(self.word)))
                        self.controller.view.hangman_label.config(image=self.controller.view.images[0], border=10,
                                                                  background='#7579e7')
                        guessed = list(self.controller.view.label_word.get())

            else:
                self.number_of_guesses += 1
                self.controller.view.hangman_label.config(image=self.controller.view.images[self.number_of_guesses])
                if self.number_of_guesses >= 10:
                    showinfo("Koniec gry!", "Twój wynik to: " + str(self.score_points))
                    self.new_game()
