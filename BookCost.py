bookCost = 24.95
numBooks = 60

def cost():
    bulkBookCost = (bookCost*0.60)*numBooks
    shippingCost = 3 + 0.75*(numBooks - 1)
    totalCost = bulkBookCost + shippingCost
    return totalCost

print(cost(),"$")
