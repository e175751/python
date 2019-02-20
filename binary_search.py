def binary_serach(card_list,card):
    low = 0
    high = len(card_list)-1
    print(high)
    while low <= high:
        mid = (low + high)//2
        if card_list[mid] == card:
            print("{0}番目に{1}があります".format(mid,card))
            return
        elif card_list[mid] < high:
            low = mid + 1
        else:
            high = mid - 1

    return

if __name__ == '__main__':
    heart_card = {2,3,5,7,11,13,17,19,23,29}
    heart_num = 11
    binary_serach(heart_card,heart_num)
