cards = [9, 10, 'J', 'K', 'Q', 4, 5, 6, 7, 8,'A', 2, 3]
converted_cards = []
for i in cards:
    if i == 'A':
        converted_cards.append(1)
    elif i == 'J':
        converted_cards.append(11)
    elif i == 'K':
        converted_cards.append(12)
    elif i == 'Q':
        converted_cards.append(13)
    else:
        converted_cards.append(i)

smallest = converted_cards[0]
sort = []
for x in converted_cards:
    if x < smallest:
        smallest = x
    else:
        pass 
        