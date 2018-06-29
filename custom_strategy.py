import sys

from market_maker.market_maker import OrderManager
from market_maker.settings import settings


class CustomOrderManager(OrderManager):
    """A sample order manager for implementing your own custom strategy"""

    def place_orders(self) -> None:
        buy_orders = []
        sell_orders = []

        for i in reversed(range(1, settings.ORDER_PAIRS + 1)):
            if not self.long_position_limit_exceeded():
                buy_orders.append(self.prepare_order(-i))
            if not self.short_position_limit_exceeded():
                sell_orders.append(self.prepare_order(i))

        self.converge_orders(buy_orders, sell_orders)


if __name__ == '__main__':
    order_manager = CustomOrderManager()

    try:
        order_manager.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
