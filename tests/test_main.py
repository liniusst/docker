# pylint: disable= missing-docstring

import unittest
from main import PizzaWinner, customer_dict


class TestPizzaWinner(unittest.TestCase):
    def setUp(self) -> None:
        self.pizza = PizzaWinner()

    def test_find_winner(self):
        self.assertEqual(self.pizza.find_winner(customer_dict), ["Karolis III"])
        self.assertNotEqual(self.pizza.find_winner(customer_dict), ["Linas"])
        self.assertNotEqual(self.pizza.find_winner(customer_dict), ["Joe Biden"])
