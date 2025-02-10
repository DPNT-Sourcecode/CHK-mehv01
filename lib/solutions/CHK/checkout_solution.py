from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    #dict for price table
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    #dict for offers: item -> (num required, discounted price)
    special_offers = {
        'A': [(5,200), (3, 130)],
        'B': [(2, 45)]
    }

    buy_get_free_offers = {
        'E': (2, 'B')
    }

    #Check for illegal input immediately
    for c in skus:
        if c not in prices:
            return -1
    
    #Count number of SKUs using Counter lib
    item_counts = Counter(skus)
    total_price = 0

    #1: Apply 'Buy X get Y free' offer
    for item, (num_required, free_item) in buy_get_free_offers.items():
        if item in item_counts:
            num_offers_triggered = item_counts[item] // num_required
            if free_item in item_counts:
                #reduce amount of items charged for
                item_counts[free_item] = max(0, item_counts[free_item] - num_offers_triggered)

    #2: Process bulk discount, applying special offers first (favouring best discount)
    for item, count in item_counts.items():
        if item in special_offers:
            #sort by best discount first
            for quantity, price in sorted(special_offers[item], reverse=True):
                while count >= quantity:
                    total_price += price
                    count -= quantity
        total_price += count * prices[item]

    return total_price
    








