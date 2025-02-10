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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21
    }

    #Special bulk discounts
    #item -> (num required, discounted price)
    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'F': [(3, 2*prices['F'])], #Buy 3F for 20 is same as buy 2F get one free
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
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

    #List of group discounts
    #item contains: ({set of items}, num of items required to trigger, discounted price)
    group_discount_items = [
        ({'S', 'T', 'X', 'Y', 'Z'}, 3, 45)
    ]

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

    #2: Apply group discount here:
    for group_items, num_required, discounted_price in group_discount_items:
        group_list = []
        for item in group_items:
            if item in item_counts:
                #for each eligible item... add each occurence
                group_list.extend([item] * item_counts[item])
        
        #Now we want to only reduce the highest priced items first!
        group_list.sort(key=lambda x: prices[x], reverse=True)

        #Apply as many group discounts as possible, starting with highest priced item
        while len(group_list) >= num_required:
            total_price += discounted_price
            #remove the first N items (i.e. the N most expensive)
            for _ in range(num_required):
                removed_item = group_list.pop(0)
                item_counts[removed_item] -= 1
        
        #Finally, any items which remain should be added back to items_count list
        for item in group_list:
            item_counts[item] += 1

    #3: Process bulk discount, applying special offers first (favouring best discount)
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
    