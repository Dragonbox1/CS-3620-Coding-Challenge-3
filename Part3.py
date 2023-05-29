def discount(price):
    return price - (price / 10)


prices = [10.00, 45.00, 76.00, 23.00]
discounted = list(map(discount, prices))
print(discounted)