import unittest

from bowling.game import BowlingGame, Frame


class TestGames(unittest.TestCase):
    example_frame = Frame(1, 5)
    strike_frame = Frame(10, 0)
    spare_frame = Frame(9, 1)
    generic_second_frame = Frame(3, 6)
    generic_frames_list = [Frame(7, 2), Frame(3, 6), Frame(4, 4), Frame(5, 3), 
                           Frame(3, 3), Frame(4, 5), Frame(8, 1), Frame(2, 6)]
    example_frames_list = [example_frame, generic_second_frame] + generic_frames_list
    example_frames_list_with_strike = [strike_frame, generic_second_frame] + generic_frames_list
    example_frames_list_with_spare = [spare_frame, generic_second_frame] + generic_frames_list
    example_frames_list_with_strike_spare = [strike_frame, Frame(4, 6)] + generic_frames_list
    example_frames_list_with_multiple_strikes = [strike_frame, strike_frame] + generic_frames_list
    example_frames_list_with_multiple_spares = [Frame(8, 2), Frame(5, 5)] + generic_frames_list

    def test_game_invalid_with_0_frames(self):
        game = BowlingGame()
        is_valid = game.is_valid_game()
        self.assertFalse(is_valid)

    def test_game_invalid_with_less_than_10_frames(self):
        game = BowlingGame()

        success = game.add_frame(self.example_frame)
        is_valid = game.is_valid_game()

        self.assertTrue(success)
        self.assertFalse(is_valid)

    def test_game_should_add_a_frame(self):
        game = BowlingGame()

        success = game.add_frame(self.example_frame)

        self.assertTrue(success)
        self.assertEqual(len(game.frames), 1)

    def test_game_should_add_a_frames_list(self):
        game = BowlingGame()

        success = game.add_frames(self.example_frames_list)

        self.assertTrue(success)
        self.assertEqual(len(game.frames), 10)

    def test_game_valid_with_10_frames(self):
        game = BowlingGame()

        success = game.add_frames(self.example_frames_list)
        is_valid = game.is_valid_game()

        self.assertTrue(success)
        self.assertTrue(is_valid)
        self.assertEqual(len(game.frames), 10)

    def test_game_should_not_pass_10_frames_with_individual_frame(self):
        game = BowlingGame()

        success_add_frame = game.add_frame(self.example_frame)
        success_add_frames = game.add_frames(self.example_frames_list)
        is_valid = game.is_valid_game()

        self.assertTrue(success_add_frame)
        self.assertFalse(success_add_frames)
        self.assertFalse(is_valid)
        self.assertEqual(len(game.frames), 1)

    def test_game_should_not_pass_10_frames_with_frames_list(self):
        game = BowlingGame()

        success_add_frames = game.add_frames(self.example_frames_list)
        success_add_more_frames = game.add_frames(self.example_frames_list)
        is_valid = game.is_valid_game()

        self.assertTrue(success_add_frames)
        self.assertFalse(success_add_more_frames)
        self.assertTrue(is_valid)
        self.assertEqual(len(game.frames), 10)

    def test_game_should_show_81_score(self):
        game = BowlingGame()

        game.add_frames(self.example_frames_list)
        score = game.score()
        
        self.assertEqual(score, 81)

    def test_game_should_show_0_score_without_frames(self):
        game = BowlingGame()

        score = game.score()
        
        self.assertEqual(score, 0)

    def test_game_should_show_score_without_10_frames(self):
        game = BowlingGame()

        game.add_frame(self.example_frame)
        score = game.score()
        
        self.assertEqual(score, 6)

    def test_strike_game_should_show_94_score(self):
        game = BowlingGame()

        game.add_frames(self.example_frames_list_with_strike)
        score = game.score()
        
        self.assertEqual(score, 94)

    def test_spare_game_should_show_88_score(self):
        game = BowlingGame()

        game.add_frames(self.example_frames_list_with_spare)
        score = game.score()
        
        self.assertEqual(score, 88)

    def test_spare_and_strike_game_should_show_103_score(self):
        game = BowlingGame()

        game.add_frames(self.example_frames_list_with_strike_spare)
        score = game.score()
        
        self.assertEqual(score, 103)

    def test_multiple_strikes_game_should_show_112_score(self):
        game = BowlingGame()

        game.add_frames(self.example_frames_list_with_multiple_strikes)
        score = game.score()
        
        self.assertEqual(score, 112)

    def test_multiple_spares_game_should_show_98_score(self):
        game = BowlingGame()

        game.add_frames(self.example_frames_list_with_multiple_spares)
        score = game.score()
        
        self.assertEqual(score, 98)

if __name__ == '__main__':
    unittest.main()
