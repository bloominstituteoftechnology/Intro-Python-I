def sockMerchant(n, ar):
    pair_dict = {}
    for num in ar:
        if num in pair_dict:
            pair_dict[num] += 1
        else:
            pair_dict[num] = 1
    print(pair_dict)
    total_pairs = 0
    for item in pair_dict.values():
        total_pairs += item//2
    print(total_pairs)
    return total_pairs


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
