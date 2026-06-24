class solution:
    orders = []
    def addOrder(self, itemName, quantity, price):
        #Write your code here..
        self.orders.append([itemName, quantity, price])
    def updateOrder(self, itemName, newQuantity, newPrice):
        #Write your code here...
        for i in self.orders:
            if i[0] == itemName:
                i[1] = newQuantity
                i[2] = newPrice
    
    def calculateTotalRevenue(self):
        #Write your code here...
        total = 0
        for itemName, quantity, price in self.orders:
            total += quantity * price
        return total