#Example: Pair sum in sorted array

def two_sum_sorted(arr, target):
    i, j = 0, len(arr) - 1

    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return i, j
        elif s < target:
            i += 1
        else:
            j -= 1

    return None

#Complexity: Time O(n), Space O(1)