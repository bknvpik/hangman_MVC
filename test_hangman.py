import unittest
import controller
import model
import view

game = controller.Controller()


class MyTestCase(unittest.TestCase):

    def test_new_game(self):
        game.model.number_of_guesses = 15
        game.model.word = "word"
        game.model.new_game()
        self.assertEqual(game.model.number_of_guesses, 0)
        self.assertNotEqual(game.model.word, "word")

    def test_controller(self):
        self.assertIsInstance(game.model, model.Model)
        self.assertIsInstance(game.view, view.View)

    def test_guess_letter(self):
        game.model.new_game()
        game.model.word = "word"
        game.model.guess_letter("a")
        self.assertEqual(game.model.number_of_guesses, 1)


if __name__ == '__main__':
    unittest.main()
