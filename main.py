# pylint: disable= missing-docstring
from typing import Dict, List


class PizzaWinner:
    def __init__(self) -> None:
        self.set_orders: int = 3
        self.set_amount: float = 40
        self.winner_list: List[str] = []

    def find_winner(self, customers_dict: Dict[str, float]) -> List[str]:
        for customer in customers_dict.keys():
            if (
                customers_dict[customer]["orders"] >= self.set_orders
                and customers_dict[customer]["order_price"] >= self.set_amount
            ):
                self.winner_list.append(customer)
        return self.winner_list


customer_dict = {
    "Linas": {"orders": 1, "order_price": 12.99},
    "Joe Biden": {"orders": 2, "order_price": 20.99},
    "Karolis III": {"orders": 3, "order_price": 40.99},
}

if __name__ == "__main__":
    winner = PizzaWinner()
    print(winner.find_winner(customer_dict))
