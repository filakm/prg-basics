def hide(card_number):
    if len(card_number) != 16 or not card_number.isdigit():
        return 'invalid card number'
    first_two = card_number[:2]
    last_fout = card_number[12:]
    middle = '*'*10
    card_mask = f'{first_two}{middle}{last_fout}'
    return card_mask