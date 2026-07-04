from collections import deque

class solution:
    def addOrderToFront(self, orders, orderId):
        # Add order to the front
        orders.appendleft(orderId)

    def addOrderToBack(self, orders, orderId):
        # Add order to the back
        orders.append(orderId)

    def removeOrderFromFront(self, orders):
        # Remove order from the front
        if orders:
            return orders.popleft()
        return None

    def removeOrderFromBack(self, orders):
        # Remove order from the back
        if orders:
            return orders.pop()
        return None

    def displayOrders(self, orders):
        # Display all orders
        for order in orders:
            print(order, end=" ")
        print()