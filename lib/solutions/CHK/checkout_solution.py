from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    #dict for price table
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    #dict for offers: item -> (num required, discounted price)
    special_offers = {
        'A': (3, 130),
        'B': (2, 45)
    }

    for c in skus:
        if c not in prices:
            return -1
    
    item_counts = Counter(skus) #count number of SKUs using Counter lib
    total_price = 0

    #process total amount, applying special offers first
    for item, count in item_counts.items():
        if item in special_offers:
            num_required, discounted_price = special_offers[item]
            offer_applied = count // num_required
            remaining = count % num_required
            total_price += (offer_applied * discounted_price) + (remaining * prices[item])
        else:
            total_price += count * prices[item]

    return total_price
            
    




