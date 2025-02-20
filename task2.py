import random

# returns a list of unique numbers between min and max
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity <= min or quantity >= max:
        return []
    return sorted(random.sample(range(min, max), quantity))

print(get_numbers_ticket(1, 1000, 3))
print(get_numbers_ticket(1, 49, 6))
