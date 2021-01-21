from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def main(self):
        self.view.main()

    def new_game(self):
        self.model.new_game()
        self.build_interface()

    def build_menu(self):
        self.view.build_menu()

    def build_interface(self):
        self.view.build_interface()

    def change_category(self):
        return self.view.change_category()

    def label_word(self):
        return self.view.label_word

    def score(self):
        return self.view.score

    def hangman_label(self):
        return self.view.hangman_label


if __name__ == '__main__':
    game = Controller()
    game.build_menu()
    game.main()
