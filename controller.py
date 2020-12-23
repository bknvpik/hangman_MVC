from model import Model
from view import View

class Controller:

    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def main(self):
        self.view.main()

    def new_game(self):
        self.view.build_menu()
        self.model.new_game()

    def change_category(self):
        return self.view.change_category()

    def label_word_get(self):
        return self.view.label_word.get()

if __name__ == '__main__':
    game = Controller()
    game.new_game()
    game.main()
