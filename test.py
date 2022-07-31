from app import Set, Score
import unittest

class TestSetWinning(unittest.TestCase):
    def test_score_grows(self):
        set = Set()
        self.assertEqual("0", set.first_player())
        set.first_players()
        self.assertEqual("15", set.first_player())
        self.assertEqual("0", set.second_player())
        set.second_players()
        self.assertEqual("15", set.secondScore())
    def test_player_1_win_when_scores_at_40(self):
        set = Set()
        set.first_players(3)
        self.assertEqual(None, set.winner())
        set.first_players()
        self.assertEqual(1, set.winner())
    def test_player_2_win_when_scores_at_40(self):
        set = Set()
        set.second_players(3)
        self.assertEqual(None, set.winner())
        set.second_players()
        self.assertEqual(2, set.winner())

class TestScoreNames(TestCase):
    def test_score_names(self):
        scores = Score()
        self.assertEqual("0", scores.scoreName(0))
        self.assertEqual("15", scores.scoreName(1))
        self.assertEqual("30", scores.scoreName(2))
        self.assertEqual("40", scores.scoreName(3))
        self.assertEqual("A", scores.scoreName(4))

        
if __name__ == '__main__':
    unittest.main()