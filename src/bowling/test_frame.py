import unittest

from bowling.frame import Frame


class TestFrames(unittest.TestCase):
    def test_first_throw_higher_than_10(self):
        frame = Frame(11, 1)
        self.assertEqual(frame.first_throw, 10)

    def test_second_throw_higher_than_10(self):
        frame = Frame(9, 11)
        self.assertEqual(frame.second_throw, 10)

    def test_first_throw_lower_than_0(self):
        frame = Frame(-1, 0)
        self.assertEqual(frame.first_throw, 0)

    def test_second_throw_lower_than_0(self):
        frame = Frame(0, -1)
        self.assertEqual(frame.second_throw, 0)

    def test_first_throw_should_be_equal_param_5(self):
        frame = Frame(5, 1)
        self.assertEqual(frame.first_throw, 5)

    def test_second_throw_should_be_equal_param_5(self):
        frame = Frame(1, 5)
        self.assertEqual(frame.second_throw, 5)

    def test_max_score(self):
        frame = Frame(9, 10)
        score = frame.score()
        self.assertEqual(score, 19)

    def test_min_score(self):
        frame = Frame(0, 0)
        score = frame.score()
        self.assertEqual(score, 0)

    def test_score_with_2_and_6_should_be_8(self):
        frame = Frame(2, 6)
        score = frame.score()
        self.assertEqual(score, 8)

    def test_frame_should_be_strike(self):
        frame = Frame(10, 0)
        is_strike = frame.is_strike()
        self.assertTrue(is_strike)

    def test_frame_should_not_be_strike(self):
        frame = Frame(0, 10)
        is_strike = frame.is_strike()
        self.assertFalse(is_strike)

    def test_frame_should_be_spare(self):
        frame = Frame(4, 6)
        is_spare = frame.is_spare()
        self.assertTrue(is_spare)

    def test_frame_should_not_be_spare(self):
        frame = Frame(3, 4)
        is_spare = frame.is_spare()
        self.assertFalse(is_spare)

    def test_frame_should_not_be_strike_and_spare(self):
        frame = Frame(10, 0)
        is_spare = frame.is_spare()
        is_strike = frame.is_strike()
        self.assertFalse(is_spare)
        self.assertTrue(is_strike)

    def test_strike_frame_should_have_10_score(self):
        frame = Frame(10, 0)
        score = frame.score()
        self.assertEqual(score, 10)

    def test_strike_throw_should_not_have_another_throw_score(self):
        frame = Frame(10, 4)
        score = frame.score()
        self.assertEqual(score, 10)
        self.assertEqual(frame.second_throw, 0)


if __name__ == '__main__':
    unittest.main()
