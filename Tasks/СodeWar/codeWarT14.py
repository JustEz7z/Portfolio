def count_positives_sum_negatives(arr):
    positive = 0
    negetive = 0
    for i in arr:
        if 1 <= i:
            positive += 1
        else:
            negetive += i
    if len(arr) == 0:
        return []
    list = [positive,negetive]
    return list