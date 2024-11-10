import unittest
from dynamic_programing import (
    Item,
    knapsack,
    _build_matrix,
    _figure_out_sack_items
)


class TestKnapsack(unittest.TestCase):
    def test_build_cache_matrix(self):
        item_list = [
            Item("P1", 2, 3)
        ]
        expected_cache_matrix = [[0,0,0,0], \
                                 [0,0,0,2]]
        self.assertEqual(_build_matrix(item_list, 3), expected_cache_matrix)
        item_list = [
            Item("P1", 2, 3),
            Item("P2", 5, 2)
        ]
        expected_cache_matrix = [[0,0,0,0], \
                                 [0,0,0,2], \
                                 [0,0,5,5]]
        self.assertEqual(_build_matrix(item_list, 3), expected_cache_matrix)

    def test_figure_out_chosen_items(self):
        item_list = [
            Item("P1", 2, 3)
        ]
        cache_matrix = [[0,0,0,0], \
                        [0,0,0,2]]
        self.assertEqual(_figure_out_sack_items(cache_matrix, item_list), \
                                                    [Item("P1", 2, 3)])
        item_list = [
            Item("P1", 2, 3),
            Item("P2", 5, 2)
        ]
        cache_matrix = [[0,0,0,0], \
                         [0,0,0,2], \
                         [0,0,5,5]]
        self.assertEqual(_figure_out_sack_items(cache_matrix, item_list), \
                                                    [Item("P2", 5, 2)])

    def test_empty_item_list(self):
        item_list = []
        self.assertEqual(knapsack(item_list, 3), ([], 0))

    def test_no_sack_capacity(self):
        item_list = [
            Item("P1", 2, 3)
        ]
        self.assertEqual(knapsack(item_list, 0), ([], 0))

    def test_one_item(self):
        item_list = [
            Item("P1", 2, 3)
        ]
        self.assertEqual(knapsack(item_list, 3), ([Item("P1", 2, 3)], 2))

    def test_many_items(self):
        item_list = [
            Item("P1", 2, 3),
            Item("P2", 2, 1),
            Item("P3", 4, 3),
            Item("P4", 5, 4),
            Item("P5", 3, 2),
        ]
        expected_sack_items = [
            Item("P2", 2, 1),
            Item("P4", 5, 4),
            Item("P5", 3, 2),
        ]
        r_sack_items, r_value = knapsack(item_list, 7)
        self.assertEqual(len(r_sack_items), len(expected_sack_items))
        for i in expected_sack_items:
            self.assertIn(i, r_sack_items)
        self.assertEqual(r_value, 10)


if __name__ == '__main__':
    unittest.main()
