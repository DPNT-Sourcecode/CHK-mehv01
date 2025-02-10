from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    #Price table for individual items
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

    #Special bulk discounts
    #item -> (num required, discounted price)
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'F': [(3, 2*prices['F'])], #Buy 3F for 20 is same as buy 2F get one free
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'U': [(4, 3*prices['U'])],
        'V': [(3, 130), (2, 90)]
    }

    #Buy X, get Y free offers
    #item -> (num required, free item)
    buy_get_free_offers = {
        'E': (2, 'B'),
        'N': (3, 'M'),
        'R': (3, 'Q')
    }

    #Check for illegal input immediately
    for c in skus:
        if c not in prices:
            return -1 #invalid SKU found, return
    
    #Count number of each SKU using Counter lib
    item_counts = Counter(skus)
    total_price = 0

    #1: Apply 'Buy X get Y free' offers
    for item, (num_required, free_item) in buy_get_free_offers.items():
        if item in item_counts: 
            num_offers_triggered = item_counts[item] // num_required
            #If the free item exists...
            if free_item in item_counts:
                #...reduce its count based on triggered offer
                item_counts[free_item] = max(0, item_counts[free_item] - num_offers_triggered)

    #2: Process bulk discount, applying special offers first (favouring best discount)
    for item, count in item_counts.items():
        if item in special_offers:
            #sort by best discount first
            for quantity, price in sorted(special_offers[item], reverse=True):
                #Loop to apply as many discounts as possible
                while count >= quantity:
                    total_price += price
                    count -= quantity

        total_price += count * prices[item] #Add any leftover items at regular price

    return total_price #return final checkout total
    
