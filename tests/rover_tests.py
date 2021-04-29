import unittest
from classes.rover import Rover


class RoverMethodTests(unittest.TestCase):

    def test_init_rover(self):
        # Arrange
        test_rover = Rover()
        # Act
        # Assert
        self.assertIsInstance(test_rover, Rover)

    
    def test_set_rover_state(self):
        initial_coords = (0,0)
        test_rover = Rover(initial_coords)

        self.assertEqual(test_rover.coords, initial_coords)