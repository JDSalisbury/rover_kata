import unittest
from classes.map_grid import GridMap


class MapMethodTests(unittest.TestCase):

    def test_init_map(self):

        under_test = GridMap()

        self.assertIsInstance(under_test, GridMap)

    def test_map_size(self):

        under_test = GridMap(10, 5)
        self.assertEqual(len(under_test.grid), 50)

    def test_place_on_grid(self):
        coords = (2, 1)
        rover = 'R'
        under_test = GridMap(3, 2)

        rover_at = under_test.place_item_at(rover, coords)

        self.assertEqual(under_test.grid[rover_at], rover)

    def test_whats_at_coords(self):
        coords = (2, 1)
        rover = 'R'
        gridMap = GridMap(10, 10)
        gridMap.place_item_at(rover, coords)


        under_test = gridMap.get_item_at(coords)

        self.assertEqual(under_test, rover)

    def test_randomly_palaced_items_on_map(self):

        gridMap = GridMap(10,10)

        gridMap.place_items_randomly(10, '@')
        gridMap.place_items_randomly(10, '+')
        print(gridMap)
        print(gridMap.random_items_list)

        self.assertIn('@', gridMap.grid)