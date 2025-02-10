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
    
    item_counts = Counter(skus) #count number of SKUs using Counter lib
    total_price = 0

    #1: Apply 'Buy X get Y free' offer
    for item, offers in special_offers.items():
        for offer in offers:
            if 

    #2: Process bulk discount, applying special offers first (favouring best discount)
    for item, count in item_counts.items():
        if item in special_offers:
            num_required, discounted_price = special_offers[item]
            offer_applied = count // num_required
            remaining = count % num_required
            total_price += (offer_applied * discounted_price) + (remaining * prices[item])
        else:
            total_price += count * prices[item]

    return total_price
            
    

