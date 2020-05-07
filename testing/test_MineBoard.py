import unittest
from Board import MineBoard as mb


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.MineBoard = mb.MineBoard(10, 8, 1, 5, True)  # Creates 10x8 minesweeper board
        # Manually adding mines to ensure that future tests remain accurate
        self.MineBoard.addMine(0, 0)
        self.MineBoard.addMine(0, 1)
        self.MineBoard.addMine(0, 2)
        self.MineBoard.addMine(1, 0)
        self.MineBoard.addMine(1, 2)
        self.MineBoard.addMine(2, 0)
        self.MineBoard.addMine(2, 1)
        self.MineBoard.addMine(2, 2)
        self.MineBoard.addMine(5, 6)
        self.MineBoard.addMine(8, 4)

    def tearDown(self):
        del self.MineBoard

    def test_has_mine(self):
        self.assertTrue(self.MineBoard.hasMine(0, 0))
        self.assertTrue(self.MineBoard.hasMine(0, 1))
        self.assertTrue(self.MineBoard.hasMine(0, 2))
        self.assertTrue(self.MineBoard.hasMine(1, 0))
        self.assertTrue(self.MineBoard.hasMine(1, 2))
        self.assertTrue(self.MineBoard.hasMine(2, 0))
        self.assertTrue(self.MineBoard.hasMine(2, 1))
        self.assertTrue(self.MineBoard.hasMine(2, 2))
        self.assertTrue(self.MineBoard.hasMine(5, 6))
        self.assertTrue(self.MineBoard.hasMine(8, 4))

    def test_is_valid_tile(self):
        self.assertFalse(self.MineBoard.isValidTile(-3, -5))
        self.assertTrue(self.MineBoard.isValidTile(2, 2))

    def test_add_and_remove_flag(self):
        self.MineBoard.addFlag(1, 1)
        self.assertTrue(self.MineBoard.hasFlag(1, 1))
        self.MineBoard.removeFlag(1, 1)
        self.assertFalse(self.MineBoard.hasFlag(1, 1))

    def test_increment_nearby(self):
        # We'll be testing the incrementNearby functions called during mine placement
        self.assertEqual(self.MineBoard.getContent(1, 1), 8)
        self.assertEqual(self.MineBoard.getContent(3, 3), 1)

    def test_can_add_and_can_remove_flag(self):
        self.assertTrue(self.MineBoard.canAddFlag(4, 4))
        self.MineBoard.addFlag(4, 4)
        self.assertTrue(self.MineBoard.canRemoveFlag(4, 4))
        self.MineBoard.uncoverExact(4, 4)
        self.assertFalse(self.MineBoard.canAddFlag(4, 4))

    def test_is_covered(self):
        self.assertTrue(self.MineBoard.isCovered(4, 4))
        self.MineBoard.uncoverExact(4, 4)
        self.assertFalse(self.MineBoard.isCovered(4, 4))

    def test_reset_game(self):
        self.MineBoard.uncoverBoard()
        self.MineBoard.resetGame()
        self.assertTrue(self.MineBoard.tile_state[0][0] == 0)

    def test_sub_attempt(self):
        current = self.MineBoard.getAttemptsRemaining()
        self.MineBoard.subAttempt()
        self.assertEqual(current-1, self.MineBoard.getAttemptsRemaining())

    def test_get_squares_uncovered(self):
        self.MineBoard.uncoverExact(5, 5)
        self.assertEqual(self.MineBoard.getSquaresUncovered(), 1)
        self.MineBoard.uncoverExact(6, 6)
        self.assertEqual(self.MineBoard.getSquaresUncovered(), 2)

    def test_get_num_flags_placed(self):
        self.assertEqual(self.MineBoard.getNumFlags(), 0)
        self.MineBoard.addFlag(5, 5)
        self.assertEqual(self.MineBoard.getNumFlags(), 1)

    def test_get_current_shown_text(self):
        self.MineBoard.uncoverBoard()
        self.assertEqual(self.MineBoard.getCurrentShownText(1, 1), "8")
        self.assertEqual(self.MineBoard.getCurrentShownText(0, 0), "*")
        self.assertEqual(self.MineBoard.getCurrentShownText(3, 3), "1")
        self.assertEqual(self.MineBoard.getCurrentShownText(4, 4), " ")

    def test_has_number(self):
        self.assertFalse(self.MineBoard.hasNumber(0, 0))
        self.assertTrue(self.MineBoard.hasNumber(1, 1))
        self.assertFalse(self.MineBoard.hasNumber(4, 4))

    def test_process_move(self):
        self.MineBoard.processMove(1, 1)
        self.assertFalse(self.MineBoard.isCovered(1, 1))
        self.assertTrue(self.MineBoard.isCovered(0, 1))
        self.MineBoard.processMove(4, 4)
        self.assertFalse(self.MineBoard.isCovered(5, 5))

    # Process blank tested within process move

    def test_uncover_all_mines(self):
        self.MineBoard.uncoverAllMines()
        self.assertTrue(self.MineBoard.hasMine(0, 0) and not self.MineBoard.isCovered(0, 0))

if __name__ == '__main__':
    unittest.main()
