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
    
    item_counts = Counter(skus)
    total_price = 0

    for item, count in item_counts.items():
        print(item, count)
        # if item in special_offers:

    return item_counts.items()
            
    



